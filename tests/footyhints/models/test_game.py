import pytest

from footyhints.models.game import Game
from footyhints.models.team import Team


class TestGameInit(object):
    def test_init(self):
        team1 = Team()
        team2 = Team()
        game = Game(home_team=team1, away_team=team2)
        assert game.home_team is team1
        assert game.away_team is team2

    def test_init_bad_home(self):
        team1 = "garbageteam"
        team2 = Team()
        with pytest.raises(ValueError) as exception_obj:
            Game(home_team=team1, away_team=team2)
        assert str(exception_obj.value) == 'home_team must be of type "Team"'

    def test_init_bad_away(self):
        team1 = Team()
        team2 = "garbageteam"
        with pytest.raises(ValueError) as exception_obj:
            Game(home_team=team1, away_team=team2)
        assert str(exception_obj.value) == 'away_team must be of type "Team"'


class TestGameWorthWatching(object):
    def setup(self):
        self.home_team = Team()
        self.away_team = Team()
        self.game = Game(home_team=self.home_team, away_team=self.away_team)

    def test_no_home_away_scores(self):
        with pytest.raises(ValueError) as exception_obj:
            self.game.worth_watching()
        assert str(exception_obj.value) == 'Score must be defined for both the home and away team'

    def test_no_home_score(self):
        self.game.away_score = 3
        with pytest.raises(ValueError) as exception_obj:
            self.game.worth_watching()
        assert str(exception_obj.value) == 'Score must be defined for the home team'

    def test_no_away_score(self):
        self.game.home_score = 2
        with pytest.raises(ValueError) as exception_obj:
            self.game.worth_watching()
        assert str(exception_obj.value) == 'Score must be defined for the away team'

        # THis should error

    # def test_0_0_game(self):

