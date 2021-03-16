from pytest import raises

from footyhints.score_plugin import ScorePlugin

from tests.footyhints.unit_test import UnitTest


class TestScorePlugin(UnitTest):
    def setup(self):
        super().setup()
        self.score_plugin = ScorePlugin()

    def test_score(self):
        with raises(NotImplementedError) as exception_obj:
            self.score_plugin.score(self.game)
        assert str(exception_obj.value) == 'Must specify a score function in the plugin'
