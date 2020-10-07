from pynsive import rlist_classes

from footyhints.plugin import Plugin, LOWEST_PRIORITY
from web.models import ScoreModification


HIGH = 'High'
MEDIUM = 'Medium'
LOW = 'Low'


class DecisionMaker():
    def __init__(self):
        self.decision_plugins = []
        self.load_decision_plugins()

    def load_decision_plugins(self):
        # wipe plugin list so we can 'refresh'
        self.decision_plugins = []
        decision_classes = rlist_classes('footyhints.plugins')
        for decision_class in decision_classes:
            # Exclude root Plugin class
            if decision_class == Plugin:
                continue
            self.decision_plugins.append(decision_class())

    def delete_score_modifications(self, game):
        for score_modification in game.score_modifications.all():
            score_modification.delete()

    def worth_watching(self, game):
        self.delete_score_modifications(game)
        # Main decision logic
        total_earned_score = 0
        total_potential_points = 0
        for decision_plugin in self.decision_plugins:
            score, reason = decision_plugin.score(game)
            if score is not None:
                importance = LOWEST_PRIORITY - decision_plugin.priority
                total_earned_score += score * importance
                # Average 75 points for each for high importance
                total_potential_points += 60 * importance
                score_modification = ScoreModification(
                    value=score,
                    reason=reason,
                    priority=decision_plugin.priority,
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
