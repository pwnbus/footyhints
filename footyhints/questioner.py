from web.models import Question
from footyhints.question_collection import QuestionCollection
from footyhints.logger import logger


class Questioner():
    def __init__(self):
        question_plugin_collection = QuestionCollection('footyhints.question_plugins')
        self.question_plugins = question_plugin_collection.plugins
        for plugin in self.question_plugins:
            logger.debug("Loaded question plugin: {}".format(plugin.__class__.__name__))

    def delete_questions(self, game):
        for question in game.questions.all():
            question.delete()

    def run(self, game):
        logger.debug("Filling in questions for game: {}".format(game))
        self.delete_questions(game)
        for question_plugin in self.question_plugins:
            answer = question_plugin.answer(game)
            question = Question(
                description=question_plugin.description,
                answer=answer,
                position=question_plugin.position,
                game=game
            )
            question.save()
            game.questions.add(question)
        game.save()
