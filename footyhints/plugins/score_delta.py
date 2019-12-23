from footyhints.plugin import Plugin


class ScoreDelta(Plugin):
    description = 'Difference between home team and away team goals'
    priority = 2

    def score(self, game):
        goal_delta = abs(game.home_team_score - game.away_team_score)
        if goal_delta == 0:
            return 100, "Close game ({})".format(goal_delta)
        if goal_delta == 1:
            return 75, "Close game ({})".format(goal_delta)
        elif goal_delta == 2:
            return 50, "Decent game ({})".format(goal_delta)
        elif goal_delta == 3:
            return 25, "Decent game ({})".format(goal_delta)
        elif goal_delta == 4:
            return 0, "OK game ({})".format(goal_delta)
        elif goal_delta == 5:
            return -25, "Blow out ({})".format(goal_delta)
        else:
            return -100, "Not a competitive game ({})".format(goal_delta)
