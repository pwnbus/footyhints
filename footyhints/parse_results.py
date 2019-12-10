from footyhints.models.team import Team
from footyhints.models.round import Round
from footyhints.models.game import Game

from footyhints.db import session


class ParseResults():
    def determine_worth_watching(self, games):
        for game in games:
            game.worth_watching()
            session.add(game)

    def parse_results(self, results):
        home_teams = [result['home_team'] for result in results]
        away_teams = [result['away_team'] for result in results]
        team_names = set(home_teams + away_teams)
        teams = {}
        for team_name in team_names:
            team = Team(name=team_name)
            teams[team_name] = team
            session.add(team)
        session.commit()
        games = []
        for match in results:
            round_obj = Round(match['match_day'])
            session.add(round_obj)
            game = Game(
                home_team=teams[match['home_team']],
                away_team=teams[match['away_team']],
                round=round_obj
            )
            game.set_score(match['home_score'], match['away_score'])
            print("Creating game\t{0} | {1}\t{2}-{3} ({4})".format(
                match['home_team'],
                match['away_team'],
                game.home_team_score,
                game.away_team_score,
                round_obj.num
            ))
            games.append(game)

        self.determine_worth_watching(games)
        session.commit()
        session.close()
