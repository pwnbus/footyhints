from footyhints.question import Question


class HomeTeamGoals(Question):
    description = "Does the home team score more than 1 goal?"

    def answer(self, game):
        if game.home_team_score >= 2:
            return "Yes"
        else:
            return "No"
