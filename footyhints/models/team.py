from sqlalchemy import Column, Integer, String

from footyhints.models.base import Base


class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __init__(self, name):
        if type(name) is not str:
            raise TypeError('Team name must be a string')
        self.name = name
