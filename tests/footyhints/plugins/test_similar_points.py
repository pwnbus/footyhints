from footyhints.plugins.similar_points import SimilarPoints

from tests.footyhints.unit_test import UnitTest


class TestSimilarPoints(UnitTest):
    def setup(self):
        super().setup()
        self.session.add(self.home_team)
        self.session.add(self.away_team)
        self.session.commit()
        self.similar_points = SimilarPoints(self.game)

    def test_description(self):
        assert self.similar_points.description == 'Proximity in points'

    def test_over_max_score(self):
        self.game.home_team.points = 0
        self.game.away_team.points = 0
        self.game.set_score(0, 0)
        score, reason = self.similar_points.score()
        assert score == 100
        assert reason == 'Same number of points in table'

    def test_middle_score(self):
        self.game.home_team.points = 3
        self.game.away_team.points = 0
        self.game.set_score(2, 2)
        score, reason = self.similar_points.score()
        assert score == 75
        assert reason == 'Close proximity in points'

    def test_two_games_diff(self):
        self.game.home_team.points = 6
        self.game.away_team.points = 0
        self.game.set_score(2, 2)
        score, reason = self.similar_points.score()
        assert score == 75
        assert reason == 'Close proximity in points'

    def test_three_games_diff(self):
        self.game.home_team.points = 9
        self.game.away_team.points = 0
        self.game.set_score(2, 2)
        score, reason = self.similar_points.score()
        assert score == 50
        assert reason == 'Nearby proximity in points'

    def test_exact_min_score(self):
        self.game.home_team.points = 30
        self.game.away_team.points = 0
        self.game.set_score(0, 0)
        score, reason = self.similar_points.score()
        assert score == -25
        assert reason == 'Large gap between teams in points'
