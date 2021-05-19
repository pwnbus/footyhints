from web.models import ScoreModification

from tests.footyhints.unit_test import UnitTest


class TestScoreModificationModel(UnitTest):
    def setup(self):
        super().setup()
        self.score_modification = ScoreModification(
            value=100,
            game=self.game,
            reason="Example reason",
            priority=1
        )

    def test_init_positive_value(self):
        assert self.score_modification.value == 100
        assert self.score_modification.reason == 'Example reason'
        assert self.score_modification.game == self.game

    def test_init_negative_value(self):
        score_modification = ScoreModification(
            value=-100,
            game=self.game,
            reason="Example reason",
            priority=1
        )
        assert score_modification.value == -100
        assert score_modification.reason == 'Example reason'
        assert score_modification.game == self.game

    def test_basic_save(self):
        assert self.score_modification.id is None
        self.score_modification.save()
        assert self.score_modification.id is not None
