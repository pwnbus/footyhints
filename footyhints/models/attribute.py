from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from footyhints.models.base import Base


class Attribute(Base):
    __tablename__ = 'attributes'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    value = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship('Game', back_populates='attributes')
