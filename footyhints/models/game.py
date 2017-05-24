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
    home_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    home_team = relationship("Team", foreign_keys=[home_team_id], backref='home_games')
    away_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    away_team = relationship("Team", foreign_keys=[away_team_id], backref='away_games')
    home_team_score = Column(Integer, nullable=True)
    away_team_score = Column(Integer, nullable=True)

    def __init__(self, home_team, away_team):
        if not type(home_team) is Team:
            raise TypeError('home_team must be of type "Team"')
        if not type(away_team) is Team:
            raise TypeError('away_team must be of type "Team"')

        self.home_team = home_team
        self.away_team = away_team
        self.home_score = None
        self.away_score = None
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

        if total_score > 5:
            return HIGH
        elif total_score > -5:
            return MEDIUM
        else:
            return LOW

    def __eq__(self, other):
        if isinstance(other, Game):
            return self.id == other.id
        return False
