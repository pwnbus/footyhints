from footyhints.score_plugin import LOWEST_PRIORITY
from web.models import ScoreModification
from footyhints.score_collection import ScoreCollection
from footyhints.logger import logger


HIGH = 'High'
MEDIUM = 'Medium'
LOW = 'Low'


class Scorer():
    def __init__(self):
        score_collection = ScoreCollection('footyhints.score_plugins')
        self.score_plugins = score_collection.plugins
        for plugin in self.score_plugins:
            logger.debug("Loaded score plugin: {}".format(plugin.__class__.__name__))

    def delete_score_modifications(self, game):
        for score_modification in game.score_modifications.all():
            score_modification.delete()

    def run(self, game):
        logger.debug("Scoring game: {}".format(game))
        self.delete_score_modifications(game)
        # Main decision logic
        total_earned_score = 0
        total_potential_points = 0
        for score_plugin in self.score_plugins:
            score, reason = score_plugin.score(game)
            if score is not None:
                importance = LOWEST_PRIORITY - score_plugin.priority
                total_earned_score += score * importance
                # Average 75 points for each for high importance
                total_potential_points += 60 * importance
                score_modification = ScoreModification(
                    value=score,
                    reason=reason,
                    priority=score_plugin.priority,
                    game=game
                )
                score_modification.save()
                game.score_modifications.add(score_modification)

        score_earned_percent = (total_earned_score / total_potential_points) * 100
        game.interest_score = float("{0:.2f}".format(score_earned_percent))

        if game.interest_score >= 100:
            game.interest_score = 100
        elif game.interest_score <= 0:
            game.interest_score = 0

        if game.interest_score >= 66:
            game.interest_level = HIGH
        elif game.interest_score >= 33:
            game.interest_level = MEDIUM
        else:
            game.interest_level = LOW

        game.save()
