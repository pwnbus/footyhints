from footyhints.plugin import Plugin


class ScoreDelta(Plugin):
    description = 'Difference between home team and away team goals'
    # Max score would be a 0 goal difference
    max_score = 100
    # Min Score would be a 0-5 game
    min_score = 0

    def score(self):
        goal_delta = abs(self.game.home_team_score - self.game.away_team_score)
        if goal_delta >= 5:
            return 0
        else:
            return abs(5 - goal_delta) * 20
