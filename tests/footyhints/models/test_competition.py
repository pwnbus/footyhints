from tests.footyhints.unit_test import UnitTest


class TestCompetitionInit(UnitTest):

    def test_name(self):
        assert self.competition.name == "English Premier League"

    def test_id(self):
        assert self.competition.id is not None

    def test_last_updated(self):
        assert self.competition.last_updated is None
        self.competition.update_timestamp()
        assert self.competition.last_updated is not None
        assert type(self.competition.last_updated is str)

    def test_teams(self):
        assert self.competition.teams.count() == 2

    def test_games(self):
        assert self.competition.games.count() == 1

    def test_logo(self):
        assert self.competition.logo == '/static/images/default_competition_logo.png'
