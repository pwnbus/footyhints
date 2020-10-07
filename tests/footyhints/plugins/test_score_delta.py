from footyhints.plugins.score_delta import ScoreDelta

from tests.footyhints.unit_test import UnitTest


class TestScoreDelta(UnitTest):
    def setup(self):
        super().setup()
        self.score_delta = ScoreDelta()

    def test_nil_nil(self):
        self.game.set_score(0, 0)
        score, reason = self.score_delta.score(self.game)
        assert score == 100
        assert reason == 'Delta between score (0)'

    def test_exact_max_score(self):
        self.game.set_score(3, 2)
        score, reason = self.score_delta.score(self.game)
        assert score == 75
        assert reason == 'Delta between score (1)'

    def test_middle_score(self):
        self.game.set_score(1, 3)
        score, reason = self.score_delta.score(self.game)
        assert score == 50
        assert reason == 'Delta between score (2)'

    def test_exact_min_score(self):
        self.game.set_score(5, 0)
        score, reason = self.score_delta.score(self.game)
        assert score == -25
        assert reason == 'Delta between score (5)'

    def test_under_min_score(self):
        self.game.set_score(8, 0)
        score, reason = self.score_delta.score(self.game)
        assert score == -100
        assert reason == 'Delta between score (8)'
