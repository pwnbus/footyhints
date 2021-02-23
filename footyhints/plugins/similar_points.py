from footyhints.plugin import Plugin


def points_at_time(team, start_time):
    total_points = 0
    for game in team.games.filter(finished=True).all():
        if game.start_time < start_time:
            if game.home_team == team:
                if game.home_team_score > game.away_team_score:
                    total_points += 3
                elif game.home_team_score == game.away_team_score:
                    total_points += 1
            elif game.away_team == team:
                if game.away_team_score > game.home_team_score:
                    total_points += 3
                elif game.away_team_score == game.home_team_score:
                    total_points += 1
    return total_points


class SimilarPoints(Plugin):
    priority = 2

    def score(self, game):
        home_points = points_at_time(game.home_team, game.start_time)
        away_points = points_at_time(game.away_team, game.start_time)
        difference = abs(home_points - away_points)
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
