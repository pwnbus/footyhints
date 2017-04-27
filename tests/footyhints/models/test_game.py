from footyhints.models.game import Game
from footyhints.models.team import Team


class TestGameInit(object):
    def test_init(self):
        team1 = Team()
        team2 = Team()
        game = Game(home_team=team1, away_team=team2)
        assert game.home_team is team1
        assert game.away_team is team2
