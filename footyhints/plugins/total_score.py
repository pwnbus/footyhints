from footyhints.plugin import Plugin


# If the game is high scoring
class HighScore(Plugin):
    def score(self):
        total_goals = self.game.home_score + self.game.away_score
        if total_goals > 3:
            return 10
        elif total_goals > 1:
            return 0
        else:
            return -8

