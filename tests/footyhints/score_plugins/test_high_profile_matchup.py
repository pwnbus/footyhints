from footyhints.score_plugins.high_profile_matchup import HighProfileMatchup

from tests.footyhints.unit_test import UnitTest
from web.models import Team, Game


class TestHighProfileMatchup(UnitTest):

    def create_tmp_game(self, home_team_name, away_team_name):
        home_team = Team(name=home_team_name)
        away_team = Team(name=away_team_name)
        return Game(home_team=home_team, away_team=away_team)

    def test_not_enough_games_matchup(self):
        self.create_previous_game(winner="Draw")
        game = self.create_current_game(winner="Winner")
        matchup = HighProfileMatchup()
        score, reason = matchup.score(game)
        assert score == 0
        assert reason == 'Too Early in Season'

    def test_high_profile_matchup(self):
        self.create_previous_game(winner="Draw")
        self.create_previous_game(winner="Draw")
        self.create_previous_game(winner="Draw")
        self.create_previous_game(winner="Draw")
        game = self.create_current_game(winner="Winner")
        matchup = HighProfileMatchup()
        score, reason = matchup.score(game)
        assert score == 100
        assert reason == 'Top 6 matchup (1 v 2)'
