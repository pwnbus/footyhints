from footyhints.plugin import Plugin


class TotalScore(Plugin):
    priority = 1

    def score(self, game):
        total_goals = game.home_team_score + game.away_team_score
        if total_goals == 0:
            return -50, "Goals (0)"
        elif total_goals == 1:
            return -25, "Goals (1)"
        elif total_goals == 2:
            return 25, "Goals ({})".format(total_goals)
        elif total_goals == 3:
            return 50, "Goals ({})".format(total_goals)
        elif total_goals == 4:
            return 75, "Goals ({})".format(total_goals)
        elif total_goals == 5:
            return 90, "Goals ({})".format(total_goals)
        elif total_goals == 6:
            return 95, "Goals ({})".format(total_goals)
        else:
            return 125, "Goals ({})".format(total_goals)
