from footyhints.plugin import Plugin


class ScoreDelta(Plugin):
    description = 'Difference between home team and away team goals'
    # Max score would be a 0 goal difference
    max_score = 5
    # Min Score would be a 0-5 game

    def score(self):
        total_goals = self.game.home_team_score + self.game.away_team_score
        goal_delta = abs(self.game.home_team_score - self.game.away_team_score)
        max_goals_delta = 5
        if goal_delta >= max_goals_delta:
            return 0
        elif goal_delta == 0:
            return self.max_score
        else:
            return int((abs(max_goals_delta - goal_delta) / max_goals_delta) * self.max_score)
