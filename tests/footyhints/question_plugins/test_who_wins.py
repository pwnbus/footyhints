from footyhints.question_plugins.who_wins import WhoWins

from tests.footyhints.unit_test import UnitTest


class TestWhoWins(UnitTest):
    def setup(self):
        super().setup()
        self.who_wins = WhoWins()

    def test_draw(self):
        self.game.set_score(0, 0)
        answer = self.who_wins.answer(self.game)
        assert answer == 'Draw'

    def test_home_team_winner(self):
        self.game.set_score(1, 0)
        answer = self.who_wins.answer(self.game)
        assert answer == 'Team #1'

    def test_away_team_winner(self):
        self.game.set_score(0, 1)
        answer = self.who_wins.answer(self.game)
        assert answer == 'Team #2'
