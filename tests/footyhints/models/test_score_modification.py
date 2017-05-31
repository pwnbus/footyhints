from footyhints.models.score_modification import ScoreModification

from tests.footyhints.unit_test import UnitTest


class TestScoreModificationInit(UnitTest):
    def test_init_positive_value(self):
        score_modification = ScoreModification(value=100, description='Goals', game=self.game)
        assert score_modification.value == 100
        assert score_modification.description == 'Goals'
        assert score_modification.game == self.game

    def test_init_negative_value(self):
        score_modification = ScoreModification(value=-100, description='Lack of Goals', game=self.game)
        assert score_modification.value == -100
        assert score_modification.description == 'Lack of Goals'
        assert score_modification.game == self.game


class TestScoreModificationSave(UnitTest):
    def test_basic_save(self):
        score_modification = ScoreModification(value=100, description='Goals', game=self.game)
        assert score_modification.id is None
        self.db.save(score_modification)
        assert score_modification.id is not None
