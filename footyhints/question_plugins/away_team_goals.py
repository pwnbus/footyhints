from footyhints.question import Question


class AwayTeamGoals(Question):
    position = 5

    def answer(self, game):
        self.description = "Does {} score more than 1 goal?".format(game.away_team.name)
        if game.away_team_score >= 2:
            return "Yes"
        else:
            return "No"
