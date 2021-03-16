from footyhints.question import Question


class WhoWins(Question):
    position = 1
    description = "Who wins?"

    def answer(self, game):
        if game.home_team_score > game.away_team_score:
            return "Home Team"
        elif game.away_team_score > game.home_team_score:
            return "Away Team"
        else:
            return "Draw"
