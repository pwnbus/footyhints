from footyhints.plugin import Plugin


def points_at_matchday(team, matchday):
    total_points = 0
    for game in team.games:
        if game.round.num < matchday:
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
        home_points = points_at_matchday(game.home_team, game.round.num)
        away_points = points_at_matchday(game.away_team, game.round.num)
        difference = abs(home_points - away_points)
        if difference == 0:
            return 100, "Proximity in points (0)"
        elif difference <= 6:
            return 75, "Proximity in points ({})".format(difference)
        elif difference <= 12:
            return 50, "Proximity in points ({})".format(difference)
        elif difference <= 18:
            return 25, "Proximity in points ({})".format(difference)
        elif difference <= 24:
            return 0, "Proximity in points ({})".format(difference)
        elif difference <= 30:
            return -25, "Proximity in points ({})".format(difference)
        elif difference <= 36:
            return -50, "Proximity in points ({})".format(difference)
        else:
            return -10, "Proximity in points ({})".format(difference)
