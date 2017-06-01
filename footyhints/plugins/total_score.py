from footyhints.plugin import Plugin


class HighScore(Plugin):
    description = "Total amount of goals in the game"

    def score(self):
        total_goals = self.game.home_team_score + self.game.away_team_score
        if total_goals == 0:
            return -10
        score_per_goal = 15
        return total_goals * score_per_goal
