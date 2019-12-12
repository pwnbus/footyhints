from footyhints.plugins.score_delta import ScoreDelta

from tests.footyhints.unit_test import UnitTest


class TestScoreDelta(UnitTest):
    def setup(self):
        super().setup()
        self.session.add(self.home_team)
        self.session.add(self.away_team)
        self.session.commit()
        self.score_delta = ScoreDelta(self.game)

    def test_description(self):
        assert self.score_delta.description == 'Difference between home team and away team goals'

    def test_nil_nil(self):
        self.game.set_score(0, 0)
        score, reason = self.score_delta.score()
        assert score == 100
        assert reason == 'Close game'

    def test_exact_max_score(self):
        self.game.set_score(3, 2)
        score, reason = self.score_delta.score()
        assert score == 75
        assert reason == 'Close game'

    def test_middle_score(self):
        self.game.set_score(1, 3)
        score, reason = self.score_delta.score()
        assert score == 50
        assert reason == 'Decent game'

    def test_exact_min_score(self):
        self.game.set_score(5, 0)
        score, reason = self.score_delta.score()
        assert score == -25
        assert reason == 'Blow out'

    def test_under_min_score(self):
        self.game.set_score(8, 0)
        score, reason = self.score_delta.score()
        assert score == -100
        assert reason == 'Not a competitive game'
