from time import time

from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from footyhints.models.base import Base


class Competition(Base):
    __tablename__ = 'competitions'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    last_updated = Column(Integer, nullable=True)
    games = relationship("Game", back_populates="competition")

    def update_timestamp(self):
        self.last_updated = int(time())
