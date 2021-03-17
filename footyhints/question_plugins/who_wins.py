from footyhints.question import Question


class WhoWins(Question):
    position = 6
    description = "Who wins?"

    def answer(self, game):
        if game.home_team_score > game.away_team_score:
            return game.home_team.name
        elif game.away_team_score > game.home_team_score:
            return game.away_team.name
        else:
            return "Draw"
