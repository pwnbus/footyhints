from footyhints.models.team import Team
from footyhints.models.round import Round
from footyhints.models.game import Game

from footyhints.db import session


class ParseResults():

    def parse_results(self, results, teams):
        team_objs = {}
        for team_name in teams:
            team_objs[team_name] = Team(name=team_name)

        for match in results:
            round_obj = Round(match['match_day'])
            session.add(round_obj)
            game = Game(home_team=team_objs[match['home_team']], away_team=team_objs[match['away_team']], round=round_obj)
            game.set_score(match['home_score'], match['away_score'])
            print("Creating game\t{0} | {1}\t{2}-{3} ({4})".format(
                match['home_team'],
                match['away_team'],
                game.home_team_score,
                game.away_team_score,
                round_obj.num
            ))
            game.worth_watching()
            session.add(game)
        session.commit()
        session.close()
