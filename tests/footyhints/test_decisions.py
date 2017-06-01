from footyhints.levels import LOW, MEDIUM, HIGH

from tests.footyhints.unit_test import UnitTest


class TestDecisionsFromScore(UnitTest):
    def test_0_0(self):
        self.game.set_score(0, 0)
        self.game.worth_watching()
        assert self.game.interest_level is LOW
        assert self.game.interest_score == 0

    def test_1_0(self):
        self.game.set_score(1, 0)
        self.game.worth_watching()
        assert self.game.interest_level is LOW
        assert self.game.interest_score == 20

    def test_1_1(self):
        self.game.set_score(1, 1)
        self.game.worth_watching()
        assert self.game.interest_level is LOW
        assert self.game.interest_score == 33

    def test_2_1(self):
        self.game.set_score(2, 1)
        self.game.worth_watching()
        assert self.game.interest_level is MEDIUM
        assert self.game.interest_score == 43

    def test_2_2(self):
        self.game.set_score(2, 2)
        self.game.worth_watching()
        assert self.game.interest_level is MEDIUM
        assert self.game.interest_score == 57

    def test_3_2(self):
        self.game.set_score(3, 2)
        self.game.worth_watching()
        assert self.game.interest_level is HIGH
        assert self.game.interest_score == 68

    def test_3_3(self):
        self.game.set_score(3, 3)
        self.game.worth_watching()
        assert self.game.interest_level is HIGH
        assert self.game.interest_score == 80

    def test_3_4(self):
        self.game.set_score(3, 4)
        self.game.worth_watching()
        assert self.game.interest_level is HIGH
        assert self.game.interest_score == 91

    def test_4_4(self):
        self.game.set_score(4, 4)
        self.game.worth_watching()
        assert self.game.interest_level is HIGH
        assert self.game.interest_score == 100
