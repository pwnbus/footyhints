from footyhints.question_plugins.nil_nil import NilNil

from tests.footyhints.unit_test import UnitTest


class TestNilNil(UnitTest):
    def setup(self):
        super().setup()
        self.nil_nil = NilNil()

    def test_nil_nil(self):
        self.game.set_score(0, 0)
        answer = self.nil_nil.answer(self.game)
        assert answer == 'Yes'

    def test_not_nil_nil(self):
        self.game.set_score(1, 0)
        answer = self.nil_nil.answer(self.game)
        assert answer == 'No'
