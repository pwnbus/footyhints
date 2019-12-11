from footyhints.plugin import Plugin


class SimilarPoints(Plugin):
    description = 'Proximity in points'

    def score(self):
        home_points = self.game.home_team.points
        away_points = self.game.away_team.points
        difference = abs(home_points - away_points)
        if difference == 0:
            return 100, "Same number of points in table"
        elif difference <= 3:
            return 50, "Close proximity in points"
        elif difference <= 6:
            return 25, "Nearby proximity in points"
        elif difference <= 9:
            return 15, "Nearby proximity in points"
        elif difference <= 15:
            return 15, "Gap between teams in points"
        elif difference <= 20:
            return 0, "Large gap between teams in points"
        else:
            return 0, "Huge gap between teams in points"
