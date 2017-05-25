from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from footyhints.models.base import Base


class Round(Base):
    __tablename__ = 'rounds'
    id = Column(Integer, primary_key=True)
    num = Column(Integer, nullable=False)
    games = relationship("Game", back_populates="round")

    def __init__(self, num):
        self.num = num
