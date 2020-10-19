from web.models import Competition, Team, Game
from footyhints.decision_maker import DecisionMaker
from footyhints.logger import logger


class ParseResults():
    def __init__(self, league_country, league_name, update):
        self.league = league_country + " " + league_name
        self.update = update

    def create_teams(self, results):
        teams = {}
        if self.update:
            db_teams = Team.objects.all()
            for team in db_teams:
                teams[team.name] = team
            return teams
        home_teams = [result['home_team'] for result in results]
        away_teams = [result['away_team'] for result in results]
        team_names = set(home_teams + away_teams)
        for team_name in team_names:
            logger.debug("Creating team: {}".format(team_name))
            team = Team(name=team_name)
            teams[team_name] = team
            team.save()
        return teams

    def get_competition(self, league_name):
        competition = Competition(name=league_name)
        if self.update:
            competition_queryset = Competition.objects.filter(name__contains=league_name)
            if competition_queryset.count() > 0:
                competition = competition_queryset[0]
                logger.debug("Found existing competition: {}".format(competition.name))
        competition.save()
        return competition

    def parse_results(self, results):
        teams = self.create_teams(results)
        decision_maker = DecisionMaker()
        competition = self.get_competition(self.league)

        for match in results:
            if self.update:
                # Look if game already exists
                home_teams_queryset = Team.objects.filter(name__contains=match['home_team'])
                if home_teams_queryset.count() > 0:
                    home_team = home_teams_queryset[0]
                    games_queryset = Game.objects.filter(team__name=home_team.name).filter(match_day=match['match_day'])
                    if games_queryset.count() > 0:
                        found_game = games_queryset[0]
                        # Existing game found (based on home_team and match_day) so skip over
                        logger.debug("Existing game found {} vs {} ({})".format(
                            found_game.home_team.name,
                            found_game.away_team.name,
                            found_game.match_day
                        ))
                        continue

            home_team = teams[match['home_team']]
            away_team = teams[match['away_team']]
            game = Game(
                home_team=teams[match['home_team']],
                away_team=teams[match['away_team']],
                match_day=match['match_day'],
                start_time=match['start_time'],
                competition=competition,
            )
            game.save()
            home_team.games.add(game)
            home_team.save()
            away_team.games.add(game)
            away_team.save()
            game.set_score(match['home_score'], match['away_score'])
            logger.info("Creating game\t{0} | {1}\t{2}-{3} ({4})".format(
                match['home_team'],
                match['away_team'],
                game.home_team_score,
                game.away_team_score,
                game.match_day
            ))
            decision_maker.worth_watching(game)
            game.save()
        competition.update_timestamp()
        competition.save()
