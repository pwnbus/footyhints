from footyhints.db import engine, session
from footyhints.models.round import Round
from footyhints.models.team import Team
from footyhints.models.game import Game
from footyhints.models.base import Base
from footyhints.models.attribute import Attribute


class UnitTest(object):
    def setup(self):
        self.session = session
        Base.metadata.create_all(engine)

        self.home_team = Team(name='Chelsea')
        self.away_team = Team(name='Manchester United')
        self.round = Round(1)
        self.game = Game(home_team=self.home_team, away_team=self.away_team, round=self.round)
        self.attribute = Attribute(name='example', value='test', description='temp example value', game=self.game)

    def teardown(self):
        Base.metadata.drop_all(engine)
        self.session.close()
