from footyhints.models.competition import Competition

from tests.footyhints.unit_test import UnitTest


class TestCompetitionInit(UnitTest):
    def test_normal_init(self):
        competition = Competition(name='Premier League')
        assert competition.name == 'Premier League'
        assert competition.games == []


class TestCompetitionLastUpdated(UnitTest):
    def test_last_updated(self):
        competition = Competition(name='Premier League')
        assert competition.last_updated is None
        competition.update_timestamp()
        assert competition.last_updated is not None
