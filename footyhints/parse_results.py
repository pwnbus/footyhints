from web.models import Competition, Team, Game
from footyhints.decision_maker import DecisionMaker


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
            team = Team(name=team_name)
            teams[team_name] = team
            team.save()
        return teams

    def get_competition(self, league_name):
        competition = Competition(name=league_name)
        if self.update:
            competition_db = Competition.objects.filter(name__contains=league_name)[0]
            if competition_db:
                competition = competition_db
        competition.save()
        return competition

    def parse_results(self, results):
        teams = self.create_teams(results)
        decision_maker = DecisionMaker()
        competition = self.get_competition(self.league)

        for match in results:
            if self.update:
                home_teams_queryset = Team.objects.filter(name__contains=match['home_team'])
                if home_teams_queryset.count() > 0:
                    home_team = home_teams_queryset[0]
                    game_found = Game.objects.filter(team__name=home_team.name).filter(match_day=match['match_day'])[0]
                    if game_found:
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
            print("Creating game\t{0} | {1}\t{2}-{3} ({4})".format(
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
