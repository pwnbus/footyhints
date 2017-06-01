from footyhints.plugin import Plugin


class NilNil(Plugin):
    description = 'The game does not have any goals'
    # Subtract 5 points if game is nil nil
    max_score = 0

    def score(self):
        total_goals = self.game.home_team_score + self.game.away_team_score
        if total_goals == 0:
            return -5
        else:
            return 0
