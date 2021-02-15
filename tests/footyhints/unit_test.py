import pytest
from web.models import Team, Competition, Game

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class UnitTest(object):
    def setup(self):
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

        # Wish this was dynamic and based on Team initializer
        # self.game.attributes.add(self.attribute)
        # self.game.score_modifications.add(self.score_modification)
        self.competition.teams.add(self.home_team)
        self.competition.teams.add(self.away_team)
        self.competition.games.add(self.game)
