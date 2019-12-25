from footyhints.plugin import Plugin


class ScoreDelta(Plugin):
    priority = 2

    def score(self, game):
        goal_delta = abs(game.home_team_score - game.away_team_score)
        if goal_delta == 0:
            return 100, "Delta between score ({})".format(goal_delta)
        if goal_delta == 1:
            return 75, "Delta between score ({})".format(goal_delta)
        elif goal_delta == 2:
            return 50, "Delta between score ({})".format(goal_delta)
        elif goal_delta == 3:
            return 25, "Delta between score ({})".format(goal_delta)
        elif goal_delta == 4:
            return 0, "Delta between score ({})".format(goal_delta)
        elif goal_delta == 5:
            return -25, "Delta between score ({})".format(goal_delta)
        else:
            return -100, "Delta between score ({})".format(goal_delta)
