from glob import glob
from os.path import join, dirname, abspath

from pytest import raises

from footyhints.models.score_modification import ScoreModification
from footyhints.decision_maker import DecisionMaker

from tests.footyhints.unit_test import UnitTest


class DecisionMakerTest(UnitTest):
    def setup(self):
        super().setup()
        self.decision = DecisionMaker()


class TestDecisionMakerLoadDecisionPlugins(DecisionMakerTest):
    def test_plugins(self):
        plugins_path = join(dirname(abspath(__file__)), '../../footyhints/plugins')
        assert len(self.decision.decision_plugins) == 0
        self.decision.load_decision_plugins(self.game)
        expected_plugin_num = len(glob(plugins_path + "/*.py")) - 1
        assert len(self.decision.decision_plugins) == expected_plugin_num


class TestDecisionMakerWorthWatching(DecisionMakerTest):
    def test_no_scores(self):
        with raises(TypeError) as exception_obj:
            self.decision.worth_watching(self.game)
        assert str(exception_obj.value) == 'Home and away scores must be set'

    def test_before_method_call(self):
        self.session.add(self.home_team)
        self.session.add(self.away_team)
        self.session.commit()
        self.game.set_score(1, 1)
        assert self.game.interest_score is None
        assert self.game.interest_level is None
        self.decision.worth_watching(self.game)
        assert type(self.game.interest_score) is float
        assert type(self.game.interest_level) is str


class TestDecisionMakerDeleteScoreModifications(DecisionMakerTest):
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
        self.decision.delete_score_modifications(self.game)
        assert len(self.game.score_modifications) == 0
