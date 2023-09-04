from web.models import Question

from tests.footyhints.unit_test import UnitTest


class TestQuestionModel(UnitTest):
    def setup_method(self):
        super().setup_method()
        self.question = Question(
            description='Test Question',
            position=10,
            answer='An answer to the question',
            game=self.game
        )

    def test_init(self):
        assert self.question.description == 'Test Question'
        assert self.question.position == 10
        assert self.question.answer == 'An answer to the question'
        assert self.question.game == self.game

    def test_save(self):
        assert self.question.id is None
        self.question.save()
        assert self.question.id is not None
