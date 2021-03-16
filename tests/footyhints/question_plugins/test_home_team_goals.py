from footyhints.question_plugins.home_team_goals import HomeTeamGoals

from tests.footyhints.unit_test import UnitTest


class TestHomeTeamGoals(UnitTest):
    def setup(self):
        super().setup()
        self.home_team_goals = HomeTeamGoals()

    def test_nil_nil(self):
        self.game.set_score(0, 0)
        answer = self.home_team_goals.answer(self.game)
        assert answer == 'No'

    def test_one_nil(self):
        self.game.set_score(1, 0)
        answer = self.home_team_goals.answer(self.game)
        assert answer == 'No'

    def test_two_nil(self):
        self.game.set_score(2, 0)
        answer = self.home_team_goals.answer(self.game)
        assert answer == 'Yes'

    def test_three_nil(self):
        self.game.set_score(3, 0)
        answer = self.home_team_goals.answer(self.game)
        assert answer == 'Yes'
