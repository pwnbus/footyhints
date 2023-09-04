import pytest
from web.models import Team, Competition, Game

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class UnitTest(object):
    def setup_method(self):
        self.competition = Competition(name="English Premier League")
        self.competition.save()
        self.home_team = Team(name="Team #1")
        self.home_team.save()
        self.away_team = Team(name="Team #2")
        self.away_team.save()
        self.game = Game(
            home_team=self.home_team,
            away_team=self.away_team,
            competition=self.competition,
            start_time=123456789,
        )
        self.game.save()
        self.home_team.games.add(self.game)
        self.home_team.save()
        self.away_team.games.add(self.game)
        self.away_team.save()

        self.competition.teams.add(self.home_team)
        self.competition.teams.add(self.away_team)
        self.competition.games.add(self.game)

        self.last_created_game_timestamp = 1594445619

    def create_game(self, start_time=None, winner="Home"):
        if start_time is None:
            self.last_created_game_timestamp += 1
            start_time = self.last_created_game_timestamp
        game = Game(home_team=self.home_team, away_team=self.away_team, start_time=start_time)
        game.save()
        if winner == "Home":
            game.set_score(1, 0)
        elif winner == "Away":
            game.set_score(0, 1)
        else:
            game.set_score(0, 0)
        self.home_team.games.add(game)
        self.home_team.save()
        self.away_team.games.add(game)
        self.away_team.save()
        return game

    def create_previous_game(self, start_time=None, winner="Home"):
        game = self.create_game(start_time=start_time, winner=winner)
        game.home_team.generate_stats(game)
        game.away_team.generate_stats(game)
        Team.generate_places()
        self.home_team.refresh_from_db()
        self.away_team.refresh_from_db()
        return game

    def create_current_game(self, start_time=None, winner="Home"):
        return self.create_game(start_time=start_time, winner=winner)
