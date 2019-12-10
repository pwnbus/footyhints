from sqlalchemy import Column, Integer, Text

from footyhints.models.base import Base


class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    points = Column(Integer, default=0)

    def __init__(self, name):
        if type(name) is not str:
            raise TypeError('Team name must be a string')
        self.name = name

    @property
    def games(self):
        return self.home_games + self.away_games
