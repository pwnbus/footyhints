from sqlalchemy import Column, Integer, String

from footyhints.models.base import Base
from footyhints.models.team import Team


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    home_team = Column(String(50), nullable=False)
    away_team = Column(String(50), nullable=False)
    home_score = Column(Integer, nullable=False)
    away_score = Column(Integer, nullable=False)

    def __init__(self, home_team, away_team):
        if not type(home_team) is Team:
            raise TypeError('home_team must be of type "Team"')
        if not type(away_team) is Team:
            raise TypeError('away_team must be of type "Team"')

        self.home_team = home_team
        self.away_team = away_team
        self.home_score = None
        self.away_score = None

    def set_score(self, home_team_score, away_team_score):
        if type(home_team_score) is not int and type(away_team_score) is not int:
            raise TypeError('Home and away scores must be integers')
        elif type(home_team_score) is not int:
            raise TypeError('Home team score must be an integer')
        elif type(away_team_score) is not int:
            raise TypeError('Away team score must be an integer')

        self.home_score = home_team_score
        self.away_score = away_team_score

    def worth_watching(self):
        if self.home_score is None and self.away_score is None:
            raise TypeError('Home and away scores must be set')

        # Main decision logic

        #   If score is 0 0, not worth watching
        if self.home_score == 0 and self.away_score == 0:
            return False

        return True
