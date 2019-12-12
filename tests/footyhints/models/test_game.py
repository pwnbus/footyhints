from glob import glob


from os.path import join, dirname, abspath

from pytest import raises

from footyhints.models.game import Game
from footyhints.models.team import Team
from footyhints.models.score_modification import ScoreModification

from tests.footyhints.unit_test import UnitTest


class TestGameInit(UnitTest):
    def test_init(self):
        assert self.game.home_team is self.home_team
        assert self.game.away_team is self.away_team
        assert self.game.round.num == 1
        assert self.game.attributes == [self.attribute]

    def test_init_bad_home(self):
        with raises(AttributeError):
            Game(home_team="garbageteam", away_team=self.away_team, round=self.round)

    def test_init_bad_away(self):
        with raises(AttributeError):
            Game(home_team=self.home_team, away_team="garbageteam", round=self.round)


class TestGameLoadDecisionPlugins(UnitTest):
    def test_plugins(self):
        plugins_path = join(dirname(abspath(__file__)), '../../../footyhints/plugins')
        assert len(self.game.decision_plugins) == 0
        self.game.load_decision_plugins()
        expected_plugin_num = len(glob(plugins_path + "/*.py")) - 1
        assert len(self.game.decision_plugins) == expected_plugin_num


class TestGameSave(UnitTest):
    def test_basic_save(self):
        assert self.game.id is None
        assert self.home_team.id is None
        assert self.away_team.id is None
        self.session.add(self.game)
        self.session.commit()
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

    def test_before_method_call(self):
        self.session.add(self.home_team)
        self.session.add(self.away_team)
        self.session.commit()
        self.game.set_score(1, 1)
        assert self.game.interest_score is None
        assert self.game.interest_level is None
        self.game.worth_watching()
        assert type(self.game.interest_score) is int
        assert type(self.game.interest_level) is str


class TestGameDeleteScoreModifications(UnitTest):
    def test_delete_scores(self):
        assert len(self.game.score_modifications) == 0
        modification1 = ScoreModification(
            value=100,
            description='test description',
            game=self.game,
            reason="Example reason",
            priority=1
        )
        self.session.add(modification1)
        modification2 = ScoreModification(
            value=10,
            description='test description again',
            game=self.game,
            reason="Example reason",
            priority=1
        )
        self.session.add(modification2)
        self.session.commit()

        assert len(self.game.score_modifications) == 2
        self.game.delete_score_modifications()
        assert len(self.game.score_modifications) == 0


class TestGameEquals(UnitTest):
    def setup(self):
        super().setup()
        self.tmp_team1 = Team(name='Chelsea')
        self.tmp_team2 = Team(name='Manchester United')
        self.tmp_game = Game(home_team=self.tmp_team1, away_team=self.tmp_team2, round=self.round)

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
