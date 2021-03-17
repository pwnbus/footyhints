from footyhints.question import Question


class HomeTeamGoals(Question):
    position = 4
    description = "Does the home team score more than 1 goal?"

    def answer(self, game):
        if game.home_team_score >= 2:
            return "Yes"
        else:
            return "No"
