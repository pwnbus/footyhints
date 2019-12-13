from footyhints.plugins.similar_points import SimilarPoints

from tests.footyhints.unit_test import UnitTest

from footyhints.models.round import Round
from footyhints.models.game import Game


class TestSimilarPoints(UnitTest):
    def setup(self):
        super().setup()
        self.session.add(self.home_team)
        self.session.add(self.away_team)
        self.session.commit()
        self.similar_points = SimilarPoints(self.game)

    def create_round(self, round_num, winner="Home"):
        round_obj = Round(round_num)
        self.session.add(round_obj)
        game = Game(home_team=self.home_team, away_team=self.away_team, round=round_obj)
        if winner == "Home":
            game.set_score(1, 0)
        else:
            game.set_score(0, 1)
        self.session.add(game)
        self.session.commit()
        return game

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
        self.game.set_score(2, 2)
        self.session.add(self.game)
        self.session.commit()
        self.create_round(2)
        game = self.create_round(3)
        similar_points = SimilarPoints(game)
        score, reason = similar_points.score()
        assert score == 75
        assert reason == 'Close proximity in points (3)'

    def test_two_games_diff(self):
        self.game.set_score(2, 2)
        self.session.add(self.game)
        self.session.commit()
        self.create_round(2)
        self.create_round(3)
        self.create_round(4)
        game = self.create_round(5)
        similar_points = SimilarPoints(game)
        score, reason = similar_points.score()
        assert score == 50
        assert reason == 'Nearby proximity in points (9)'
