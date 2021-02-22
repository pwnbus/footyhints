from footyhints.plugin import Plugin


class ScoreDelta(Plugin):
    priority = 2

    def score(self, game):
        goal_delta = abs(game.home_team_score - game.away_team_score)
        if goal_delta == 0:
            points = 100
        elif goal_delta == 1:
            points = 75
        elif goal_delta == 2:
            points = 50
        elif goal_delta == 3:
            points = 25
        elif goal_delta == 4:
            points = 0
        elif goal_delta == 5:
            points = -25
        else:
            points = -100

        return points, "Delta between score ({})".format(goal_delta)
