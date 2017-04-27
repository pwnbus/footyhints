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

