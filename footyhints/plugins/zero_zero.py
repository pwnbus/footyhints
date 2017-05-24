from footyhints.plugin import Plugin


# If the game is 0 - 0, not worth watching
class ZeroZero(Plugin):
    def decision(self):
        if self.game.home_score == 0 and self.game.away_score == 0:
            return False
        return None
