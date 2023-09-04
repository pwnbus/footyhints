from footyhints.score_plugins.similar_points import SimilarPoints

from tests.footyhints.unit_test import UnitTest


class TestSimilarPoints(UnitTest):
    def setup_method(self):
        super().setup_method()

    def test_over_max_score(self):
        self.create_previous_game(winner="Draw")
        game = self.create_current_game(winner="Winner")
        similar_points = SimilarPoints()
        score, reason = similar_points.score(game)
        assert score == 100
        assert reason == 'Proximity in points (0)'

    def test_middle_score(self):
        self.create_previous_game()
        game = self.create_current_game()
        similar_points = SimilarPoints()
        score, reason = similar_points.score(game)
        assert score == 75
        assert reason == 'Proximity in points (3)'

    def test_three_games_diff(self):
        self.create_previous_game()
        self.create_previous_game()
        self.create_previous_game()
        self.create_previous_game(winner="Away")
        self.create_previous_game()
        game = self.create_current_game()
        similar_points = SimilarPoints()
        score, reason = similar_points.score(game)
        assert score == 50
        assert reason == 'Proximity in points (9)'
