from footyhints.plugins.similar_points import SimilarPoints

from tests.footyhints.unit_test import UnitTest

from web.models import Game


class TestSimilarPoints(UnitTest):
    def setup(self):
        super().setup()
        self.similar_points = SimilarPoints()

    def create_game(self, start_time, winner="Home"):
        game = Game(home_team=self.home_team, away_team=self.away_team, start_time=start_time)
        game.save()
        if winner == "Home":
            game.set_score(1, 0)
        else:
            game.set_score(0, 1)
        self.home_team.games.add(game)
        self.home_team.save()
        self.away_team.games.add(game)
        self.away_team.save()
        return game

    def test_over_max_score(self):
        self.game.home_team.points = 0
        self.game.away_team.points = 0
        self.game.set_score(0, 0)
        score, reason = self.similar_points.score(self.game)
        assert score == 100
        assert reason == 'Proximity in points (0)'

    def test_middle_score(self):
        self.game.set_score(2, 2)
        self.create_game(1594445619)
        game = self.create_game(1594445620)
        similar_points = SimilarPoints()
        score, reason = similar_points.score(game)
        assert score == 75
        assert reason == 'Proximity in points (3)'

    def test_two_games_diff(self):
        self.game.set_score(2, 2)
        self.game.save()
        # self.session.add(self.game)
        # self.session.commit()
        self.create_game(1594445619)
        self.create_game(1594445620)
        self.create_game(1594445621)
        game = self.create_game(1594445622)
        similar_points = SimilarPoints()
        score, reason = similar_points.score(game)
        assert score == 50
        assert reason == 'Proximity in points (9)'
