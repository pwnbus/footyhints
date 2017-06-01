from footyhints.plugins.nil_nil import NilNil

from tests.footyhints.unit_test import UnitTest


class TestNilNil(UnitTest):
    def setup(self):
        super().setup()
        self.nil_nil = NilNil(self.game)

    def test_description(self):
        assert self.nil_nil.description == 'The game does not have any goals'

    def test_nil_nil(self):
        self.game.set_score(0, 0)
        assert self.nil_nil.score() == -5

    def test_other_score(self):
        self.game.set_score(1, 3)
        assert self.nil_nil.score() == 0
