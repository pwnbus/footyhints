import pytest

from footyhints.models.round import Round
from footyhints.models.team import Team
from footyhints.models.game import Game

from tests.footyhints.unit_test import UnitTest


class TestTeamInit(UnitTest):
    def test_normal_init(self):
        team = Team(name='Chelsea')
        assert team.name == 'Chelsea'
        assert team.games == []

    def test_bad_name(self):
        with pytest.raises(TypeError) as exception_obj:
            Team(name=123)
        assert str(exception_obj.value) == 'Team name must be a string'


class TestTeamSave(UnitTest):
    def test_normal_save(self):
        assert self.home_team.id is None
        self.session.add(self.home_team)
        self.session.commit()
        assert self.home_team.id == 1
        assert self.home_team.points == 0

    def test_normal_save_with_one_game(self):
        self.session.add(self.game)
        self.session.commit()
        assert self.home_team.id == 1
        assert self.home_team.games == [self.game]
        assert self.home_team.home_games == [self.game]
        assert self.home_team.away_games == []
        assert self.away_team.games == [self.game]
        assert self.away_team.home_games == []
        assert self.away_team.away_games == [self.game]


class TestTeamGames(UnitTest):
    def test_multiple_games(self):
        team1 = Team(name='Chelsea')
        team2 = Team(name='Manchester United')
        team3 = Team(name='Arsenal')
        team4 = Team(name='Liverpool')
        round1 = Round(1)
        game1 = Game(home_team=team1, away_team=team2, round=round1, start_time=1594445619)
        self.session.add(game1)
        game2 = Game(home_team=team3, away_team=team1, round=round1, start_time=1594445620)
        self.session.add(game2)
        game3 = Game(home_team=team1, away_team=team4, round=round1, start_time=1594445621)
        self.session.add(game3)
        game4 = Game(home_team=team4, away_team=team1, round=round1, start_time=1594445622)
        self.session.add(game4)
        game5 = Game(home_team=team4, away_team=team2, round=round1, start_time=1594445623)
        self.session.add(game5)
        self.session.commit()
        assert team1.games == [game1, game3, game2, game4]
        assert team2.games == [game1, game5]
        assert team3.games == [game2]
        assert team4.games == [game4, game5, game3]
