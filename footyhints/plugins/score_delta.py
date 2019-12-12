from footyhints.plugin import Plugin


class ScoreDelta(Plugin):
    description = 'Difference between home team and away team goals'
    priority = 2

    def score(self):
        goal_delta = abs(self.game.home_team_score - self.game.away_team_score)
        if goal_delta == 0:
            return 100, "Close game"
        if goal_delta == 1:
            return 75, "Close game"
        elif goal_delta == 2:
            return 50, "Decent game"
        elif goal_delta == 3:
            return 25, "Decent game"
        elif goal_delta == 4:
            return 0, "OK game"
        elif goal_delta == 5:
            return -25, "Blow out"
        else:
            return -100, "Not a competitive game"
