from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from pynsive import rlist_classes

from footyhints.models.base import Base
from footyhints.models.team import Team
from footyhints.plugin import Plugin
from footyhints.levels import LOW, MEDIUM, HIGH


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    round_id = Column(Integer, ForeignKey('rounds.id'))
    round = relationship('Round', back_populates='games')
    home_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    home_team = relationship("Team", foreign_keys=[home_team_id], backref='home_games')
    away_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    away_team = relationship("Team", foreign_keys=[away_team_id], backref='away_games')
    home_team_score = Column(Integer, nullable=True)
    away_team_score = Column(Integer, nullable=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.decision_plugins = []

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

        self.home_team_score = home_team_score
        self.away_team_score = away_team_score

    def worth_watching(self):
        if self.home_team_score is None and self.away_team_score is None:
            raise TypeError('Home and away scores must be set')

        # Main decision logic
        self.load_decision_plugins()
        total_score = 0
        for decision_plugin in self.decision_plugins:
            score = decision_plugin.score()
            if score is not None:
                total_score += score

        self.interest_score = total_score
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
