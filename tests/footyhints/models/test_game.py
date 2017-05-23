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

    def test_no_scores(self):
        with pytest.raises(ValueError) as exception_obj:
            self.game.worth_watching()
        assert str(exception_obj.value) == 'Home and away scores must be set'

    def test_bad_scores(self):
        with pytest.raises(ValueError) as exception_obj:
            self.game.set_score('abcd', 'someother')
        assert str(exception_obj.value) == 'Home and away scores must be integers'

    def test_bad_home_score(self):
        with pytest.raises(ValueError) as exception_obj:
            self.game.set_score('abcd', 4)
        assert str(exception_obj.value) == 'Home team score must be an integer'

    def test_bad_away_score(self):
        with pytest.raises(ValueError) as exception_obj:
            self.game.set_score(2, 'abcd')
        assert str(exception_obj.value) == 'Away team score must be an integer'

    def test_0_0_game(self):
        self.game.set_score(0, 0)
        assert self.game.worth_watching() is False

    def test_3_4_game(self):
        self.game.set_score(3, 4)
        assert self.game.worth_watching() is True
