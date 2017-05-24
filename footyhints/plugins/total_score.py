from footyhints.plugin import Plugin


# If the game is high scoring
class HighScore(Plugin):
    def score(self):
        total_goals = self.game.home_team_score + self.game.away_team_score
        if total_goals > 6:
            return 100
        elif total_goals > 4:
            return 50
        elif total_goals > 3:
            return 10
        elif total_goals > 2:
            return 0
        elif total_goals > 1:
            return -40
        else:
            return -100
