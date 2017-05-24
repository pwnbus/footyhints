from footyhints.levels import LOW, MEDIUM, HIGH

from tests.footyhints.unit_test import UnitTest


class TestDecisionsFromScore(UnitTest):
    def test_0_0(self):
        self.game.set_score(0, 0)
        assert self.game.worth_watching() is LOW

    def test_1_1(self):
        self.game.set_score(1, 1)
        assert self.game.worth_watching() is MEDIUM

    def test_3_4(self):
        self.game.set_score(3, 4)
        assert self.game.worth_watching() is HIGH
