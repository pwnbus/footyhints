from footyhints.plugins.high_profile_matchup import HighProfileMatchup

from tests.footyhints.unit_test import UnitTest
from footyhints.models.round import Round
from footyhints.models.team import Team
from footyhints.models.game import Game


class TestHighProfileMatchup(UnitTest):

    def create_tmp_game(self, home_team_name, away_team_name):
        home_team = Team(name=home_team_name)
        away_team = Team(name=away_team_name)
        round_obj = Round(1)
        return Game(home_team=home_team, away_team=away_team, round=round_obj)

    def test_description(self):
        matchup = HighProfileMatchup(self.game)
        assert matchup.description == 'High Profile Matchups'

    def test_high_profile_matchup(self):
        game = self.create_tmp_game('Liverpool FC', 'Manchester United FC')
        matchup = HighProfileMatchup(game)
        assert matchup.score() == 100

    def test_reverse_high_profile_matchup(self):
        game = self.create_tmp_game('Manchester United FC', 'Liverpool FC')
        matchup = HighProfileMatchup(game)
        assert matchup.score() == 100

    def test_other_matchup(self):
        game = self.create_tmp_game('Chelsea FC', 'Everton FC')
        matchup = HighProfileMatchup(game)
        assert matchup.score() == 0
