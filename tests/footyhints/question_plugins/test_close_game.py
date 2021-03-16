from footyhints.question_plugins.close_game import CloseGame

from tests.footyhints.unit_test import UnitTest


class TestCloseGame(UnitTest):
    def setup(self):
        super().setup()
        self.close_game = CloseGame()

    def test_nil_nil(self):
        self.game.set_score(0, 0)
        answer = self.close_game.answer(self.game)
        assert answer == 'Yes'

    def test_one_nil(self):
        self.game.set_score(1, 0)
        answer = self.close_game.answer(self.game)
        assert answer == 'Yes'

    def test_two_nil(self):
        self.game.set_score(2, 0)
        answer = self.close_game.answer(self.game)
        assert answer == 'Yes'

    def test_three_nil(self):
        self.game.set_score(3, 0)
        answer = self.close_game.answer(self.game)
        assert answer == 'No'
