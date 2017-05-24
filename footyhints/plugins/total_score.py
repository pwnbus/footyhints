from footyhints.plugin import Plugin


class HighScore(Plugin):
    def score(self):
        total_goals = self.game.home_team_score + self.game.away_team_score
        score_per_goal = 15
        return total_goals * score_per_goal
