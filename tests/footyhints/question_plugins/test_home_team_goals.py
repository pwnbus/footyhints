from footyhints.question_plugins.home_team_goals import HomeTeamGoals

from tests.footyhints.unit_test import UnitTest


class TestHomeTeamGoals(UnitTest):
    def setup_method(self):
        super().setup_method()
        self.plugin = HomeTeamGoals()

    def test_nil_nil(self):
        self.game.set_score(0, 0)
        answer = self.plugin.answer(self.game)
        assert answer == 'No'
        assert self.plugin.description == 'Does Team #1 score more than 1 goal?'

    def test_one_nil(self):
        self.game.set_score(1, 0)
        answer = self.plugin.answer(self.game)
        assert answer == 'No'
        assert self.plugin.description == 'Does Team #1 score more than 1 goal?'

    def test_two_nil(self):
        self.game.set_score(2, 0)
        answer = self.plugin.answer(self.game)
        assert answer == 'Yes'
        assert self.plugin.description == 'Does Team #1 score more than 1 goal?'

    def test_three_nil(self):
        self.game.set_score(3, 0)
        answer = self.plugin.answer(self.game)
        assert answer == 'Yes'
        assert self.plugin.description == 'Does Team #1 score more than 1 goal?'
