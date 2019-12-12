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
    description = 'Proximity in points'
    priority = 2

    def score(self):
        home_points = points_at_matchday(self.game.home_team, self.game.round.num)
        away_points = points_at_matchday(self.game.away_team, self.game.round.num)
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
