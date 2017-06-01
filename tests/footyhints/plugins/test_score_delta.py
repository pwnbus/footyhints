from footyhints.plugins.score_delta import ScoreDelta

from tests.footyhints.unit_test import UnitTest


class TestScoreDelta(UnitTest):
    def setup(self):
        super().setup()
        self.score_delta = ScoreDelta(self.game)

    def test_description(self):
        assert self.score_delta.description == 'Difference between home team and away team goals'

    def test_exact_max_score(self):
        self.game.set_score(0, 0)
        assert self.score_delta.score() == self.score_delta.max_score

    def test_middle_score(self):
        self.game.set_score(1, 3)
        assert self.score_delta.score() == 3

    def test_exact_min_score(self):
        self.game.set_score(5, 0)
        assert self.score_delta.score() == 0

    def test_under_min_score(self):
        self.game.set_score(8, 0)
        assert self.score_delta.score() == 0
