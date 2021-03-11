from tests.footyhints.unit_test import UnitTest


class TestTeamModelInit(UnitTest):

    def test_name(self):
        assert self.home_team.name == 'Team #1'

    def test_points(self):
        assert self.home_team.points == 0

    def test_games(self):
        assert self.home_team.games.count() == 1

    def test_logo(self):
        assert self.home_team.logo == '/static/images/default_team_logo.png'
