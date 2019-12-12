from footyhints.plugins.total_score import TotalScore

from tests.footyhints.unit_test import UnitTest


class TestTotalScore(UnitTest):
    def setup(self):
        super().setup()
        self.session.add(self.home_team)
        self.session.add(self.away_team)
        self.session.commit()
        self.total_score = TotalScore(self.game)

    def test_description(self):
        assert self.total_score.description == 'Total amount of goals'

    def test_over_max_score(self):
        self.game.set_score(10, 10)
        score, reason = self.total_score.score()
        assert score == 125
        assert reason == 'Tons of goals'

    def test_exact_max_score(self):
        self.game.set_score(4, 4)
        score, reason = self.total_score.score()
        assert score == 125
        assert reason == 'Tons of goals'

    def test_middle_score(self):
        self.game.set_score(2, 2)
        score, reason = self.total_score.score()
        assert score == 75
        assert reason == 'Decent amount of goals'

    def test_exact_min_score(self):
        self.game.set_score(0, 0)
        score, reason = self.total_score.score()
        assert score == -50
        assert reason == 'No goals'
