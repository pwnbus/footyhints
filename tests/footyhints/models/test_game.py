from pytest import raises

from footyhints.models.game import Game
from footyhints.models.team import Team

from tests.footyhints.unit_test import UnitTest


class TestGameInit(UnitTest):
    def test_init(self):
        team1 = Team(name='Chelsea')
        team2 = Team(name='Manchester United')
        game = Game(home_team=team1, away_team=team2)
        assert game.home_team is team1
        assert game.away_team is team2

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
        self.home_team = Team(name='Chelsea')
        self.away_team = Team(name='Manchester United')
        self.game = Game(home_team=self.home_team, away_team=self.away_team)
        assert len(self.game.decision_plugins) == 1


class TestGameSave(UnitTest):
    def test_basic_save(self):
        team1 = Team(name='Chelsea')
        team2 = Team(name='Manchester United')
        game = Game(home_team=team1, away_team=team2)
        assert game.id is None
        assert team1.id is None
        assert team2.id is None
        self.db.save(game)
        assert game.id == 1
        assert team1.id == 1
        assert team2.id == 2


class TestGameSetScore(UnitTest):
    def setup(self):
        super(TestGameSetScore, self).setup()
        self.home_team = Team(name='Chelsea')
        self.away_team = Team(name='Manchester United')
        self.game = Game(home_team=self.home_team, away_team=self.away_team)

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
        home_team = Team(name='Chelsea')
        away_team = Team(name='Manchester United')
        game = Game(home_team=home_team, away_team=away_team)
        with raises(TypeError) as exception_obj:
            game.worth_watching()
        assert str(exception_obj.value) == 'Home and away scores must be set'
