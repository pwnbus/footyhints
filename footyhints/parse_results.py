from footyhints.models.team import Team
from footyhints.models.game import Game

from footyhints.db import session
from footyhints.decision_maker import DecisionMaker


class ParseResults():

    def create_teams(self, results):
        home_teams = [result['home_team'] for result in results]
        away_teams = [result['away_team'] for result in results]
        team_names = set(home_teams + away_teams)
        teams = {}
        for team_name in team_names:
            team = Team(name=team_name)
            teams[team_name] = team
            session.add(team)
        session.commit()
        return teams

    def parse_results(self, results):
        teams = self.create_teams(results)
        decision_maker = DecisionMaker()
        for match in results:
            game = Game(
                home_team=teams[match['home_team']],
                away_team=teams[match['away_team']],
                match_day=match['match_day'],
                start_time=match['start_time']
            )
            game.set_score(match['home_score'], match['away_score'])
            print("Creating game\t{0} | {1}\t{2}-{3} ({4})".format(
                match['home_team'],
                match['away_team'],
                game.home_team_score,
                game.away_team_score,
                game.match_day
            ))
            decision_maker.worth_watching(game)
            session.add(game)
            session.commit()
        session.close()
