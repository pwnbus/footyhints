from footyhints.plugin import Plugin


class TotalScore(Plugin):
    description = 'Total amount of goals'
    priority = 1

    def score(self, game):
        total_goals = game.home_team_score + game.away_team_score
        if total_goals == 0:
            return -50, "No goals"
        elif total_goals == 1:
            return -25, "A goal"
        elif total_goals == 2:
            return 25, "Couple of goals ({})".format(total_goals)
        elif total_goals == 3:
            return 50, "Few goals ({})".format(total_goals)
        elif total_goals == 4:
            return 75, "Decent amount of goals ({})".format(total_goals)
        elif total_goals == 5:
            return 90, "Good amount of goals ({})".format(total_goals)
        elif total_goals == 6:
            return 95, "Lots of goals ({})".format(total_goals)
        else:
            return 125, "Tons of goals ({})".format(total_goals)
