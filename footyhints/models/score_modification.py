from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from footyhints.models.base import Base


class ScoreModification(Base):
    __tablename__ = 'score_modifications'
    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship('Game', back_populates='score_modifications')
