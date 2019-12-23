from pytest import raises

from footyhints.plugin import Plugin

from tests.footyhints.unit_test import UnitTest


class TestPlugin(UnitTest):
    def setup(self):
        super().setup()
        self.plugin = Plugin()

    def test_description(self):
        with raises(NotImplementedError) as exception_obj:
            self.plugin.description()
        assert str(exception_obj.value) == 'Must specify a description property in the plugin'

    def test_score(self):
        with raises(NotImplementedError) as exception_obj:
            self.plugin.score(self.game)
        assert str(exception_obj.value) == 'Must specify a score function in the plugin'
