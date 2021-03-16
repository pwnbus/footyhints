from footyhints.score_plugin import ScorePlugin


class TotalScore(ScorePlugin):
    priority = 1

    def score(self, game):
        total_goals = game.home_team_score + game.away_team_score
        if total_goals == 0:
            points = -50
        elif total_goals == 1:
            points = -25
        elif total_goals == 2:
            points = 25
        elif total_goals == 3:
            points = 50
        elif total_goals == 4:
            points = 75
        elif total_goals == 5:
            points = 90
        elif total_goals == 6:
            points = 95
        else:
            points = 125

        return points, "Goals ({})".format(total_goals)
