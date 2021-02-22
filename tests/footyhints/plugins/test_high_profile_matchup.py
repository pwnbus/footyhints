from footyhints.plugins.high_profile_matchup import HighProfileMatchup

from tests.footyhints.unit_test import UnitTest
from web.models import Team, Game


class TestHighProfileMatchup(UnitTest):

    def create_tmp_game(self, home_team_name, away_team_name):
        home_team = Team(name=home_team_name)
        away_team = Team(name=away_team_name)
        return Game(home_team=home_team, away_team=away_team)

    def test_high_profile_matchup(self):
        game = self.create_tmp_game('Liverpool', 'Manchester United')
        matchup = HighProfileMatchup()
        score, reason = matchup.score(game)
        assert score == 100
        assert reason == 'Big matchup'

    def test_reverse_high_profile_matchup(self):
        game = self.create_tmp_game('Manchester United', 'Liverpool')
        matchup = HighProfileMatchup()
        score, reason = matchup.score(game)
        assert score == 100
        assert reason == 'Big matchup'

    def test_other_matchup(self):
        game = self.create_tmp_game('Chelsea', 'Everton')
        matchup = HighProfileMatchup()
        score, reason = matchup.score(game)
        assert score == 0
        assert reason == 'Not a big matchup'
