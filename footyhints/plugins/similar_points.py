from footyhints.plugin import Plugin


class SimilarPoints(Plugin):
    description = 'Proximity in points'
    priority = 2

    def score(self):
        home_points = self.game.home_team.points
        away_points = self.game.away_team.points
        difference = abs(home_points - away_points)
        if difference == 0:
            return 100, "Same number of points in table"
        elif difference <= 6:
            return 75, "Close proximity in points"
        elif difference <= 12:
            return 50, "Nearby proximity in points"
        elif difference <= 18:
            return 25, "Nearby proximity in points"
        elif difference <= 24:
            return 0, "Gap between teams in points"
        elif difference <= 30:
            return -25, "Large gap between teams in points"
        elif difference <= 36:
            return -50, "Large gap between teams in points"
        else:
            return -10, "Huge gap between teams in points"
