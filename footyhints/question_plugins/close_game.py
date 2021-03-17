from footyhints.question import Question


class CloseGame(Question):
    position = 3
    description = "Is it a close game?"

    def answer(self, game):
        goal_delta = abs(game.home_team_score - game.away_team_score)
        if goal_delta <= 2:
            return "Yes"
        else:
            return "No"
