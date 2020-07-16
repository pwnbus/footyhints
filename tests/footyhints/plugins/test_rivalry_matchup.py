from footyhints.plugins.rivalry_matchup import RivalryMatchup

from tests.footyhints.unit_test import UnitTest
from footyhints.models.team import Team
from footyhints.models.game import Game


class TestRivalryMatchup(UnitTest):

    def create_tmp_game(self, home_team_name, away_team_name):
        home_team = Team(name=home_team_name)
        away_team = Team(name=away_team_name)
        return Game(home_team=home_team, away_team=away_team, match_day=1)

    def test_rivalry_matchup(self):
        game = self.create_tmp_game('Liverpool FC', 'Manchester United FC')
        matchup = RivalryMatchup()
        score, reason = matchup.score(game)
        assert score == 100
        assert reason == 'Rivalry matchup'

    def test_reverse_rivalry_matchup(self):
        game = self.create_tmp_game('Manchester United FC', 'Liverpool FC')
        matchup = RivalryMatchup()
        score, reason = matchup.score(game)
        assert score == 100
        assert reason == 'Rivalry matchup'

    def test_other_matchup(self):
        game = self.create_tmp_game('Chelsea FC', 'Everton FC')
        matchup = RivalryMatchup()
        score, reason = matchup.score(game)
        assert score == 0
        assert reason == 'Not a rivalry matchup'
