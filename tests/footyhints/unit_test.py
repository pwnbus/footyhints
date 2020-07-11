from footyhints.db import session, create_db, delete_db
from footyhints.models.round import Round
from footyhints.models.team import Team
from footyhints.models.game import Game
from footyhints.models.attribute import Attribute


class UnitTest(object):
    def setup(self):
        self.session = session
        delete_db()
        create_db()
        self.home_team = Team(name='Chelsea')
        self.away_team = Team(name='Manchester United')
        self.round = Round(1)
        self.game = Game(home_team=self.home_team, away_team=self.away_team, round=self.round, start_time=1594445619)
        self.attribute = Attribute(name='example', value='test', description='temp example value', game=self.game)

    def teardown(self):
        self.session.close()
        delete_db()
