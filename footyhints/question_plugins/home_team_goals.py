from footyhints.question import Question


class HomeTeamGoals(Question):
    position = 4
    position = 4

    def answer(self, game):
        self.description = "Does {} score more than 1 goal?".format(game.home_team.name)
        if game.home_team_score >= 2:
            return "Yes"
        else:
            return "No"
