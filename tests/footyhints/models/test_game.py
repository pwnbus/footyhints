from pytest import raises

from footyhints.models.game import Game
from footyhints.models.team import Team

from tests.footyhints.unit_test import UnitTest


class TestGameInit(UnitTest):
    def test_init(self):
        assert self.game.home_team is self.home_team
        assert self.game.away_team is self.away_team

    def test_init_bad_home(self):
        team1 = "garbageteam"
        team2 = Team(name='Chelsea')
        with raises(TypeError) as exception_obj:
            Game(home_team=team1, away_team=team2)
        assert str(exception_obj.value) == 'home_team must be of type "Team"'

    def test_init_bad_away(self):
        team1 = Team(name='Chelsea')
        team2 = "garbageteam"
        with raises(TypeError) as exception_obj:
            Game(home_team=team1, away_team=team2)
        assert str(exception_obj.value) == 'away_team must be of type "Team"'


class TestGameLoadDecisionPlugins(UnitTest):
    def test_plugins(self):
        assert len(self.game.decision_plugins) == 1


class TestGameSave(UnitTest):
    def test_basic_save(self):
        assert self.game.id is None
        assert self.home_team.id is None
        assert self.away_team.id is None
        self.db.save(self.game)
        assert self.game.id == 1
        assert self.home_team.id == 1
        assert self.away_team.id == 2


class TestGameSetScore(UnitTest):
    def test_bad_scores(self):
        with raises(TypeError) as exception_obj:
            self.game.set_score('abcd', 'someother')
        assert str(exception_obj.value) == 'Home and away scores must be integers'

    def test_bad_home_score(self):
        with raises(TypeError) as exception_obj:
            self.game.set_score('abcd', 4)
        assert str(exception_obj.value) == 'Home team score must be an integer'

    def test_bad_away_score(self):
        with raises(TypeError) as exception_obj:
            self.game.set_score(2, 'abcd')
        assert str(exception_obj.value) == 'Away team score must be an integer'


class TestGameWorthWatching(UnitTest):
    def test_no_scores(self):
        with raises(TypeError) as exception_obj:
            self.game.worth_watching()
        assert str(exception_obj.value) == 'Home and away scores must be set'


class TestGameEquals(UnitTest):
    def setup(self):
        super(TestGameEquals, self).setup()
        self.tmp_team1 = Team(name='team1')
        self.tmp_team2 = Team(name='team2')
        self.tmp_game = Game(home_team=self.tmp_team1, away_team=self.tmp_team2)

    def test_equal_games(self):
        self.db.save(self.game)
        self.db.save(self.tmp_game)
        self.tmp_game.id = self.game.id
        assert self.game == self.tmp_game

    def test_nonequal_games(self):
        self.db.save(self.game)
        self.db.save(self.tmp_game)
        self.tmp_game.id = self.game.id + 1
        assert self.game != self.tmp_game
