from footyhints.models.round import Round

from tests.footyhints.unit_test import UnitTest


class TestRoundInit(UnitTest):
    def test_normal_init(self):
        round_obj = Round(1)
        assert round_obj.num == 1
        assert round_obj.games == []


class TestRoundSave(UnitTest):
    def test_normal_save(self):
        round_obj = Round(1)
        assert round_obj.id is None
        self.db.save(round_obj)
        assert round_obj.id == 1
