from footyhints.question_plugins.any_goals_scored import AnyGoalsScored

from tests.footyhints.unit_test import UnitTest


class TestNilNil(UnitTest):
    def setup(self):
        super().setup()
        self.plugin = AnyGoalsScored()

    def test_nil_nil(self):
        self.game.set_score(0, 0)
        answer = self.plugin.answer(self.game)
        assert answer == 'No'

    def test_not_nil_nil(self):
        self.game.set_score(1, 0)
        answer = self.plugin.answer(self.game)
        assert answer == 'Yes'
