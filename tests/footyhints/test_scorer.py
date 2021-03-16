from web.models import ScoreModification
from footyhints.scorer import Scorer

from tests.footyhints.unit_test import UnitTest


class ScorerTest(UnitTest):
    def setup(self):
        super().setup()
        self.scorer = Scorer()


class TestScoreWorthWatching(ScorerTest):

    def test_before_method_call(self):
        self.game.set_score(1, 1)
        assert self.game.interest_score is None
        assert self.game.interest_level is None
        self.scorer.run(self.game)
        assert type(self.game.interest_score) is float
        assert type(self.game.interest_level) is str


class TestScoreDeleteScoreModifications(ScorerTest):
    def test_delete_scores(self):
        assert self.game.score_modifications.count() == 0
        modification1 = ScoreModification(
            value=100,
            game=self.game,
            reason="Example reason",
            priority=1
        )
        modification1.save()
        self.game.score_modifications.add(modification1)
        modification2 = ScoreModification(
            value=10,
            game=self.game,
            reason="Example reason",
            priority=1
        )
        modification2.save()
        self.game.score_modifications.add(modification2)
        self.game.save()
        assert self.game.score_modifications.count() == 2
        self.scorer.delete_score_modifications(self.game)
        assert self.game.score_modifications.count() == 0
