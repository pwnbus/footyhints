from footyhints.question import Question


class AnyGoalsScored(Question):
    position = 2
    description = "Are goals scored?"

    def answer(self, game):
        if game.home_team_score == 0 and game.away_team_score == 0:
            return "No"
        else:
            return "Yes"
