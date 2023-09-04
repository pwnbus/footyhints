from pytest import raises

from web.models import Game, Team

from tests.footyhints.unit_test import UnitTest


class GameTest(UnitTest):
    def setup_method(self):
        super().setup_method()


class TestGameModelInit(UnitTest):

    def test_competition(self):
        assert self.game.competition.name == 'English Premier League'

    def test_start_time(self):
        assert self.game.start_time == 123456789

    def test_home_team(self):
        assert self.game.home_team.name == 'Team #1'

    def test_away_team(self):
        assert self.game.away_team.name == 'Team #2'

    def test_interest_score(self):
        assert self.game.interest_score is None

    def test_interest_level(self):
        assert self.game.interest_level is None

    def test_date_from_start_time(self):
        assert self.game.date_from_start_time == 'Thursday 29 November 1973'

    def test_init_bad_home(self):
        with raises(ValueError):
            Game(home_team="garbageteam", away_team=self.away_team, start_time=1594445619, competition=self.competition)

    def test_init_bad_away(self):
        with raises(ValueError):
            Game(home_team=self.home_team, away_team="garbageteam", start_time=1594445619, competition=self.competition)


class TestGameSetScore(GameTest):
    def test_bad_scores(self):
        with raises(TypeError) as exception_obj:
            self.game.set_score('abcd', 'someother')
        assert str(exception_obj.value) == 'Home and away scores must be integers'

    def test_bad_home_score(self):
        with raises(TypeError) as exception_obj:
            self.game.set_score('abcd', 4)
        assert str(exception_obj.value) == 'Home team score must be an integer'

    def test_bad_away_score(self):
        with raises(TypeError) as exception_obj:
            self.game.set_score(2, 'abcd')
        assert str(exception_obj.value) == 'Away team score must be an integer'


class TestGameEquals(GameTest):
    def setup_method(self):
        super().setup_method()
        self.tmp_team1 = Team(name='Team #1')
        self.tmp_team1.save()
        self.tmp_team2 = Team(name='Team #2')
        self.tmp_team2.save()
        self.tmp_game = Game(home_team=self.tmp_team1, away_team=self.tmp_team2, start_time=123456789, competition=self.competition)

    def test_equal_games(self):
        self.game.save()
        self.tmp_game.save()
        self.tmp_game.id = self.game.id
        assert self.game == self.tmp_game

    def test_nonequal_games(self):
        self.game.save()
        self.tmp_game.save()
        self.tmp_game.id = self.game.id + 1
        assert self.game != self.tmp_game

    def test_nonequal_objects(self):
        self.game.save()
        assert self.game != 'abcd'
