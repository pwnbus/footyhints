from footyhints.plugins.total_score import TotalScore

from tests.footyhints.unit_test import UnitTest


class TestTotalScore(UnitTest):
    def setup(self):
        super().setup()
        self.total_score = TotalScore()

    def test_over_max_score(self):
        self.game.set_score(10, 10)
        score, reason = self.total_score.score(self.game)
        assert score == 125
        assert reason == 'Goals (20)'

    def test_exact_max_score(self):
        self.game.set_score(4, 4)
        score, reason = self.total_score.score(self.game)
        assert score == 125
        assert reason == 'Goals (8)'

    def test_middle_score(self):
        self.game.set_score(2, 2)
        score, reason = self.total_score.score(self.game)
        assert score == 75
        assert reason == 'Goals (4)'

    def test_exact_min_score(self):
        self.game.set_score(0, 0)
        score, reason = self.total_score.score(self.game)
        assert score == -50
        assert reason == 'Goals (0)'
