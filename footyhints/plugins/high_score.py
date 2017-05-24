from footyhints.plugin import Plugin


# If the game is high scoring
class HighScore(Plugin):
    def decision(self):
        total_goals = self.game.home_score + self.game.away_score
        if total_goals > 3:
            return True
        return None
