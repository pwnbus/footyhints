from footyhints.question_plugins.who_wins import WhoWins

from tests.footyhints.unit_test import UnitTest


class TestWhoWins(UnitTest):
    def setup_method(self):
        super().setup_method()
        self.plugin = WhoWins()

    def test_draw(self):
        self.game.set_score(0, 0)
        answer = self.plugin.answer(self.game)
        assert answer == 'Draw'
        assert self.plugin.description == 'Who wins?'

    def test_home_team_winner(self):
        self.game.set_score(1, 0)
        answer = self.plugin.answer(self.game)
        assert answer == 'Team #1'
        assert self.plugin.description == 'Who wins?'

    def test_away_team_winner(self):
        self.game.set_score(0, 1)
        answer = self.plugin.answer(self.game)
        assert answer == 'Team #2'
        assert self.plugin.description == 'Who wins?'
