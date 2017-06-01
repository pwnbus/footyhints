from footyhints.plugin import Plugin


class TotalScore(Plugin):
    description = 'Total amount of goals'
    # Max score would be 8 total goals in the game
    max_score = 90
    # Min score would be 0 goals scored

    def score(self):
        total_goals = self.game.home_team_score + self.game.away_team_score
        max_num_goals = 8
        if total_goals >= max_num_goals:
            return self.max_score
        elif total_goals == 0:
            return 0
        else:
            return int((total_goals / max_num_goals) * self.max_score)
