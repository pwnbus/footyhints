from footyhints.plugin import Plugin


class TotalScore(Plugin):
    description = 'Total amount of goals'
    # Max score would be 8 total goals in the game
    max_score = 120
    # Min Score would be a 0-0 game
    min_score = -10

    def score(self):
        total_goals = self.game.home_team_score + self.game.away_team_score
        if total_goals == 0:
            return -10
        elif total_goals >= 8:
            return 120
        else:
            score_per_goal = 15
            return total_goals * score_per_goal
