from footyhints.question_plugins.one_nil import OneNil

from tests.footyhints.unit_test import UnitTest


class TestOneNil(UnitTest):
    def setup_method(self):
        super().setup_method()
        self.plugin = OneNil()

    def test_nil_nil(self):
        self.game.set_score(0, 0)
        answer = self.plugin.answer(self.game)
        assert answer == 'No'
        assert self.plugin.description == 'Is there more than 1 goal scored?'

    def test_one_nil(self):
        self.game.set_score(1, 0)
        answer = self.plugin.answer(self.game)
        assert answer == 'No'
        assert self.plugin.description == 'Is there more than 1 goal scored?'

    def test_two_nil(self):
        self.game.set_score(2, 0)
        answer = self.plugin.answer(self.game)
        assert answer == 'Yes'
        assert self.plugin.description == 'Is there more than 1 goal scored?'

    def test_one_one(self):
        self.game.set_score(1, 1)
        answer = self.plugin.answer(self.game)
        assert answer == 'Yes'
        assert self.plugin.description == 'Is there more than 1 goal scored?'
