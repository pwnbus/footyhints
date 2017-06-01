from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from pynsive import rlist_classes

from footyhints.db import session
from footyhints.models.base import Base
from footyhints.models.team import Team
from footyhints.models.attribute import Attribute
from footyhints.models.round import Round
from footyhints.models.score_modification import ScoreModification

from footyhints.plugin import Plugin, MAX_PLUGIN_SCORE
from footyhints.levels import LOW, MEDIUM, HIGH


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    round_id = Column(Integer, ForeignKey('rounds.id'))
    round = relationship(Round, back_populates='games')
    attributes = relationship(Attribute, back_populates="game")
    score_modifications = relationship(ScoreModification, back_populates="game")
    home_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    home_team = relationship(Team, foreign_keys=[home_team_id], backref='home_games')
    away_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    away_team = relationship(Team, foreign_keys=[away_team_id], backref='away_games')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.decision_plugins = []

    def get_attribute_by_name(self, name):
        for attribute in self.attributes:
            if attribute.name == name:
                attribute_value = attribute.value
                if attribute_value:
                    return int(attribute_value)

    @property
    def home_team_score(self):
        return self.get_attribute_by_name('home_score')

    @property
    def away_team_score(self):
        return self.get_attribute_by_name('away_score')

    def load_decision_plugins(self):
        # wipe plugin list so we can 'refresh'
        self.decision_plugins = []
        decision_classes = rlist_classes('footyhints.plugins')
        for decision_class in decision_classes:
            # Exclude root Plugin class
            if decision_class == Plugin:
                continue
            self.decision_plugins.append(decision_class(self))

    def set_score(self, home_team_score, away_team_score):
        if type(home_team_score) is not int and type(away_team_score) is not int:
            raise TypeError('Home and away scores must be integers')
        elif type(home_team_score) is not int:
            raise TypeError('Home team score must be an integer')
        elif type(away_team_score) is not int:
            raise TypeError('Away team score must be an integer')

        home_score = Attribute(name='home_score', value=str(home_team_score), description='Home Team Score', game=self)
        session.add(home_score)
        away_score = Attribute(name='away_score', value=str(away_team_score), description='Away Team Score', game=self)
        session.add(away_score)
        session.commit()

    def delete_score_modifications(self):
        for score_modification in self.score_modifications:
            session.delete(score_modification)
        session.commit()

    def worth_watching(self):
        if self.home_team_score is None and self.away_team_score is None:
            raise TypeError('Home and away scores must be set')
        self.delete_score_modifications()
        # Main decision logic
        self.load_decision_plugins()
        total_max_score = 0
        for decision_plugin in self.decision_plugins:
            total_max_score += decision_plugin.max_score
            # We give additional bonus points for 'importance'
            score = decision_plugin.score() + (5 * (decision_plugin.max_score / MAX_PLUGIN_SCORE))
            if score is not None:
                score_modification = ScoreModification(value=score, description=decision_plugin.description)
                self.score_modifications.append(score_modification)
                session.add(score_modification)
        session.commit()

        total_earned_score = 0
        for score_modification in self.score_modifications:
            total_earned_score += score_modification.value

        score_earned_percent = int((total_earned_score / total_max_score) * 100)
        self.interest_score = score_earned_percent

        if self.interest_score > 100:
            self.interest_score = 100
        elif self.interest_score < 0:
            self.interest_score = 0

        self.interest_level = LOW
        if self.interest_score > 66:
            self.interest_level = HIGH
        elif self.interest_score > 33:
            self.interest_level = MEDIUM

    def __eq__(self, other):
        if isinstance(other, Game):
            return (
                self.id == other.id and
                self.round == other.round and
                self.home_team.name == other.home_team.name and
                self.away_team.name == other.away_team.name
            )
        return False
