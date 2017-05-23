import pytest

from footyhints.models.team import Team


class TestTeamInit(object):
    def test_normal_init(self):
        team = Team(name='Chelsea')
        assert team.name == 'Chelsea'

    def test_bad_name(self):
        with pytest.raises(ValueError) as exception_obj:
            Team(name=123)
        assert str(exception_obj.value) == 'Team name must be a string'
