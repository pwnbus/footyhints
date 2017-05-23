from footyhints.db import db
from footyhints.models.team import Team
from footyhints.models.game import Game


class UnitTest(object):
    def setup(self):
        self.db = db
        self.db.connect()
        self.db.setup()

        self.home_team = Team(name='Chelsea')
        self.away_team = Team(name='Manchester United')
        self.game = Game(home_team=self.home_team, away_team=self.away_team)

    def teardown(self):
        self.db.destroy()
        self.db.disconnect()