from footyhints.models.game import Game
from footyhints.models.team import Team

from tests.footyhints.unit_test import UnitTest


class TestZeroZero(UnitTest):
    def setup(self):
        super(TestZeroZero, self).setup()
        self.home_team = Team(name='Chelsea')
        self.away_team = Team(name='Manchester United')
        self.game = Game(home_team=self.home_team, away_team=self.away_team)

    def test_decision_0_0(self):
        self.game.set_score(0, 0)
        assert self.game.worth_watching() is False

    def test_decision_1_1(self):
        self.game.set_score(1, 1)
        assert self.game.worth_watching() is True

    def test_decision_3_4(self):
        self.game.set_score(3, 4)
        assert self.game.worth_watching() is True
