from pytest import raises

from footyhints.plugin import Plugin

from tests.footyhints.unit_test import UnitTest


class TestPlugin(UnitTest):
    def setup(self):
        super(TestPlugin, self).setup()
        self.plugin = Plugin(self.game)

    def test_init(self):
        assert self.plugin.game == self.game

    def test_decision(self):
        with raises(NotImplementedError) as exception_obj:
            self.plugin.decision()
        assert str(exception_obj.value) == 'Must specify a decision function in plugin'