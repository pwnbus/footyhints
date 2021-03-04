from footyhints.plugin import Plugin


class SimilarPoints(Plugin):
    priority = 2

    def score(self, game):
        difference = abs(game.home_team.points - game.away_team.points)
        if difference == 0:
            points = 100
        elif difference <= 6:
            points = 75
        elif difference <= 12:
            points = 50
        elif difference <= 18:
            points = 25
        elif difference <= 24:
            points = 0
        elif difference <= 30:
            points = -25
        elif difference <= 36:
            points = -50
        else:
            points = -10

        return points, "Proximity in points ({})".format(difference)
