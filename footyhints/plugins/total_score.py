from footyhints.plugin import Plugin


# If the game is high scoring
class HighScore(Plugin):
    def score(self):
        total_goals = self.game.home_score + self.game.away_score
        if total_goals > 6:
            return 10
        elif total_goals > 4:
            return 7
        elif total_goals > 3:
            return 3
        elif total_goals > 2:
            return 0
        elif total_goals > 1:
            return -4
        else:
            return -8
