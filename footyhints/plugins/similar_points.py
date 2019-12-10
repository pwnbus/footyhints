from footyhints.plugin import Plugin


class SimilarPoints(Plugin):
    description = 'Proximity in points'
    # Max score would be teams have same points
    max_score = 90
    # Min score if teams are > 10 points away

    def score(self):
        home_points = self.game.home_team.points
        away_points = self.game.away_team.points
        difference = abs(home_points - away_points)
        if difference == 0:
            return self.max_score
        elif difference <= 3:
            return 50
        elif difference <= 6:
            return 25
        elif difference <= 9:
            return 15
        else:
            return 0
