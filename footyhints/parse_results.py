import requests
import datetime

from django.core import files
from django.utils.text import slugify
from io import BytesIO

from web.models import Competition, Team, Game
from footyhints.decision_maker import DecisionMaker
from footyhints.logger import logger


class ParseResults():
    def __init__(self, league_country, league_name, update):
        self.league = league_country + " " + league_name
        self.update = update
        self.decision_maker = DecisionMaker()

    def create_teams(self, teams_data):
        teams = {}
        if self.update:
            db_teams = Team.objects.all()
            for team in db_teams:
                teams[team.name] = team
            return teams
        sorted_team_names = sorted(teams_data)
        for sorted_name in sorted_team_names:
            team_data = teams_data[sorted_name]
            logger.debug("Creating team: {}".format(sorted_name))
            team = Team(name=sorted_name)
            if team_data['logo_url']:
                logger.debug("Downloading team logo from {0}".format(team_data['logo_url']))
                resp = requests.get(team_data['logo_url'])
                if resp.ok:
                    fp = BytesIO()
                    fp.write(resp.content)
                    file_type = team_data['logo_url'].split(".")[-1]
                    file_name = "{}.{}".format(slugify(team.name), file_type)
                    team.logo_image.save(file_name, files.File(fp))
                else:
                    logger.error("Received {0} when downloading team image".format(resp.text))
            teams[sorted_name] = team
            team.save()
        return teams

    def get_competition(self, league_name, logo_url):
        competition = Competition(name=league_name)
        if self.update:
            competition_queryset = Competition.objects.filter(name__contains=league_name)
            if competition_queryset.count() > 0:
                competition = competition_queryset[0]
                logger.debug("Found existing competition: {}".format(competition.name))
        else:
            if logo_url:
                logger.debug("Downloading competition logo from {0}".format(logo_url))
                resp = requests.get(logo_url)
                if resp.ok:
                    fp = BytesIO()
                    fp.write(resp.content)
                    file_type = logo_url.split(".")[-1]
                    file_name = "{}.{}".format(slugify(competition.name), file_type)
                    competition.logo_image.save(file_name, files.File(fp))
                else:
                    logger.error("Received {0} when downloading competition image".format(resp.text))
        competition.save()
        return competition

    def find_game(self, match):
        # Look if game already exists
        home_teams_queryset = Team.objects.filter(name__contains=match['home_team'])
        if home_teams_queryset.count() > 0:
            home_team = home_teams_queryset[0]
            games_queryset = Game.objects.filter(team__name=home_team.name).filter(start_time=match['start_time'])
            if games_queryset.count() > 0:
                found_game = games_queryset[0]
                # Existing game found (based on home_team and start_time) so skip over
                logger.debug("Existing game found {} vs {} ({})".format(
                    found_game.home_team.name,
                    found_game.away_team.name,
                    found_game.start_time
                ))
                return found_game
        return None

    def localize_timestamp(self, timestamp):
        time_fmt = "%Y-%m-%d %H:%M:%S"
        time_obj = datetime.datetime.fromtimestamp(timestamp)
        return time_obj.strftime(time_fmt)

    def parse_game(self, competition, teams, game_data):
        if not self.update:
            home_team = teams[game_data['home_team']]
            home_team.refresh_from_db()
            away_team = teams[game_data['away_team']]
            away_team.refresh_from_db()
            game = Game(
                home_team=teams[game_data['home_team']],
                away_team=teams[game_data['away_team']],
                start_time=game_data['start_time'],
                competition=competition,
                stadium=game_data['stadium'],
                city=game_data['city'],
                referee=game_data['referee'],
            )
            game.save()
            home_team.games.add(game)
            home_team.save()
            away_team.games.add(game)
            away_team.save()
            selected_game = game
        else:
            found_game = self.find_game(game_data)
            if found_game:
                if found_game.finished:
                    return
                elif 'home_score' not in game_data and 'away_score' not in game_data:
                    # Game isn't finished
                    return
            selected_game = found_game
        if 'home_score' in game_data and 'away_score' in game_data:
            # Game is finished, so run it through decision maker
            selected_game.set_score(game_data['home_score'], game_data['away_score'])
            logger.info("Creating finished game\t{0} | {1}\t{2}-{3} ({4})".format(
                game_data['home_team'],
                game_data['away_team'],
                selected_game.home_team_score,
                selected_game.away_team_score,
                self.localize_timestamp(selected_game.start_time),
            ))
            self.decision_maker.worth_watching(selected_game)
            selected_game.home_team.generate_stats(selected_game)
            selected_game.away_team.generate_stats(selected_game)
            Team.generate_places()
        else:
            logger.info("Creating upcoming game\t{0} | {1}\t ({2})".format(
                game_data['home_team'],
                game_data['away_team'],
                self.localize_timestamp(selected_game.start_time)
            ))
        selected_game.save()

    def parse_results(self, results):
        for competition_name, competition_data in results['competitions'].items():
            teams = self.create_teams(competition_data['teams'])
            competition = self.get_competition(competition_name, competition_data['logo_url'])
            for finished_game_data in sorted(competition_data['finished_games'], key=lambda game: game['start_time']):
                self.parse_game(competition, teams, finished_game_data)
            for upcoming_game_data in sorted(competition_data['upcoming_games'], key=lambda game: game['start_time']):
                self.parse_game(competition, teams, upcoming_game_data)

            competition.update_timestamp()
            competition.save()
