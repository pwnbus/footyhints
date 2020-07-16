from sqlalchemy import Column, Integer, Float, ForeignKey, Text
from sqlalchemy.orm import relationship

from footyhints.db import session
from footyhints.models.base import Base
from footyhints.models.team import Team
from footyhints.models.attribute import Attribute
from footyhints.models.score_modification import ScoreModification


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    match_day = Column(Integer, nullable=False)
    attributes = relationship(Attribute, back_populates="game")
    score_modifications = relationship(ScoreModification, back_populates="game")
    home_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    home_team = relationship(Team, foreign_keys=[home_team_id], backref='home_games')
    away_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    away_team = relationship(Team, foreign_keys=[away_team_id], backref='away_games')
    start_time = Column(Integer, nullable=False)
    interest_score = Column(Float, nullable=True)
    interest_level = Column(Text, nullable=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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

    def set_score(self, home_team_score, away_team_score):
        if type(home_team_score) is not int and type(away_team_score) is not int:
            raise TypeError('Home and away scores must be integers')
        elif type(home_team_score) is not int:
            raise TypeError('Home team score must be an integer')
        elif type(away_team_score) is not int:
            raise TypeError('Away team score must be an integer')

        if home_team_score > away_team_score:
            self.home_team.points += 3
        elif home_team_score == away_team_score:
            self.home_team.points += 1
            self.away_team.points += 1
        else:
            self.away_team.points += 3
        session.add(self.home_team)
        session.add(self.away_team)

        home_score = Attribute(name='home_score', value=str(home_team_score), description='Home Team Score', game=self)
        session.add(home_score)
        away_score = Attribute(name='away_score', value=str(away_team_score), description='Away Team Score', game=self)
        session.add(away_score)
        session.commit()

    def __eq__(self, other):
        if isinstance(other, Game):
            return self.id == other.id and self.match_day == other.match_day and self.home_team.name == other.home_team.name and self.away_team.name == other.away_team.name
        return False
