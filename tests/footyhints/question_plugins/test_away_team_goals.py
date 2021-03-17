from footyhints.question_plugins.away_team_goals import AwayTeamGoals

from tests.footyhints.unit_test import UnitTest


class TestAwayTeamGoals(UnitTest):
    def setup(self):
        super().setup()
        self.plugin = AwayTeamGoals()

    def test_nil_nil(self):
        self.game.set_score(0, 0)
        answer = self.plugin.answer(self.game)
        assert answer == 'No'
        assert self.plugin.description == 'Does Team #2 score more than 1 goal?'

    def test_nil_one(self):
        self.game.set_score(0, 1)
        answer = self.plugin.answer(self.game)
        assert answer == 'No'
        assert self.plugin.description == 'Does Team #2 score more than 1 goal?'

    def test_nil_two(self):
        self.game.set_score(0, 2)
        answer = self.plugin.answer(self.game)
        assert answer == 'Yes'
        assert self.plugin.description == 'Does Team #2 score more than 1 goal?'

    def test_nil_three(self):
        self.game.set_score(0, 3)
        answer = self.plugin.answer(self.game)
        assert answer == 'Yes'
        assert self.plugin.description == 'Does Team #2 score more than 1 goal?'
