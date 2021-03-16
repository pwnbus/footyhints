from footyhints.question import Question


class AwayTeamGoals(Question):
    position = 6
    description = "Does the away team score more than 1 goal?"

    def answer(self, game):
        if game.away_team_score >= 2:
            return "Yes"
        else:
            return "No"
