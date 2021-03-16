from footyhints.question import Question


class NilNil(Question):
    description = "Is it a nil-nil draw?"

    def answer(self, game):
        if game.home_team_score == 0 and game.away_team_score == 0:
            return "Yes"
        else:
            return "No"
