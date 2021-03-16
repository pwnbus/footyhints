from footyhints.question import Question


class OneNil(Question):
    description = "Is there only 1 goal scored?"

    def answer(self, game):
        goal_total = game.home_team_score + game.away_team_score
        if goal_total == 1:
            return "Yes"
        else:
            return "No"
