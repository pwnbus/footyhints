from pytest import raises

from footyhints.models.game import Game
from footyhints.models.team import Team

from footyhints.decision_maker import DecisionMaker

from tests.footyhints.unit_test import UnitTest


class GameTest(UnitTest):
    def setup(self):
        super().setup()
        self.decision = DecisionMaker


class TestGameInit(UnitTest):
    def test_init(self):
        assert self.game.home_team is self.home_team
        assert self.game.away_team is self.away_team
        assert self.game.match_day == 1
        assert self.game.start_time == 1594445619
        assert self.game.attributes == [self.attribute]

    def test_init_bad_home(self):
        with raises(AttributeError):
            Game(home_team="garbageteam", away_team=self.away_team, match_day=1, start_time=1594445619)

    def test_init_bad_away(self):
        with raises(AttributeError):
            Game(home_team=self.home_team, away_team="garbageteam", match_day=1, start_time=1594445619)


class TestGameSave(GameTest):
    def test_basic_save(self):
        assert self.game.id is None
        assert self.home_team.id is None
        assert self.away_team.id is None
        self.session.add(self.game)
        self.session.commit()
        assert self.game.id == 1
        assert self.home_team.id == 1
        assert self.away_team.id == 2


class TestGameSetScore(GameTest):
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


class TestGameEquals(GameTest):
    def setup(self):
        super().setup()
        self.tmp_team1 = Team(name='Chelsea')
        self.tmp_team2 = Team(name='Manchester United')
        self.tmp_game = Game(home_team=self.tmp_team1, away_team=self.tmp_team2, match_day=1, start_time=1594445619)

    def test_equal_games(self):
        self.session.add(self.game)
        self.session.add(self.tmp_game)
        self.session.commit()
        self.tmp_game.id = self.game.id
        assert self.game == self.tmp_game

    def test_nonequal_games(self):
        self.session.add(self.game)
        self.session.add(self.tmp_game)
        self.session.commit()
        self.tmp_game.id = self.game.id + 1
        assert self.game != self.tmp_game

    def test_nonequal_objects(self):
        self.session.add(self.game)
        self.session.commit()
        assert self.game != 'abcd'
