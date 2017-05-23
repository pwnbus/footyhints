from pytest import raises

from footyhints.plugin import Plugin

from footyhints.models.game import Game
from footyhints.models.team import Team


class TestPlugin(object):
    def setup(self):
        team1 = Team(name='Chelsea')
        team2 = Team(name='Manchester United')
        self.game = Game(home_team=team1, away_team=team2)
        self.plugin = Plugin(self.game)

    def test_init(self):
        assert self.plugin.game == self.game

    def test_decision(self):
        with raises(NotImplementedError) as exception_obj:
            self.plugin.decision()
        assert str(exception_obj.value) == 'Must specify a decision function in plugin'
