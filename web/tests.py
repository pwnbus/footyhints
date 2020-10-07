from django.test import TestCase

from .models import Competition, Team, Game, Attribute, ScoreModification


class UnitTestCase(TestCase):
    def setUp(self):
        self.competition = Competition(name="English Premier League")
        self.competition.save()
        self.team_1 = Team(name="Team #1")
        self.team_1.save()
        self.team_2 = Team(name="Team #2")
        self.team_2.save()
        self.game = Game(
            home_team=self.team_1,
            away_team=self.team_2,
            competition=self.competition,
            start_time=123456789,
            match_day=1
        )
        self.game.save()

        # Wish this was dynamic and based on Team initializer
        # self.game.attributes.add(self.attribute)
        # self.game.score_modifications.add(self.score_modification)
        self.competition.teams.add(self.team_1)
        self.competition.teams.add(self.team_2)
        self.competition.games.add(self.game)

# Competition model
class CompetitionModelInitTest(UnitTestCase):

    def test_name(self):
        self.assertEqual(self.competition.name, "English Premier League")

    def test_id(self):
        self.assertEqual(self.competition.id, 1)

    def test_last_updated(self):
        self.assertIsNone(self.competition.last_updated)
        self.competition.update_timestamp()
        self.assertIsNotNone(self.competition.last_updated)

    def test_teams(self):
        self.assertEqual(self.competition.teams.count(), 2)

    def test_games(self):
        self.assertEqual(self.competition.games.count(), 1)


# Game model
class GameModelInitTest(UnitTestCase):

    def test_competition(self):
        self.assertEqual(self.game.competition.name, "English Premier League")

    def test_match_day(self):
        self.assertEqual(self.game.match_day, 1)

    def test_start_time(self):
        self.assertEqual(self.game.start_time, 123456789)

    def test_home_team(self):
        self.assertEqual(self.game.home_team.name, 'Team #1')

    def test_away_team(self):
        self.assertEqual(self.game.away_team.name, 'Team #2')

    def test_interest_score(self):
        self.assertIsNone(self.game.interest_score)

    def test_interest_level(self):
        self.assertIsNone(self.game.interest_level)

    def test_date_from_start_time(self):
        self.assertEqual(self.game.date_from_start_time, "Thursday 29 November 1973")

    # def test_attributes(self):
    #     self.assertEqual(self.game.attributes.count(), 1)

    # def test_score_modifications(self):
    #     self.assertEqual(self.game.score_modifications.count(), 1)

class GameModelSetScoreTest(UnitTestCase):

    def test_score(self):
        self.game.set_score(2, 1)
        self.game.save()
        self.assertEqual(self.team_1.points, 3)
        self.assertEqual(self.team_2.points, 0)
        self.assertEqual(self.game.home_team_score, 2)
        self.assertEqual(self.game.away_team_score, 1)
        # self.assertEqual(self.game.attributes.count(), 2)


# Team model
class TeamModelInitTest(UnitTestCase):

    def test_name(self):
        self.assertEqual(self.team_1.name, "Team #1")

    def test_points(self):
        self.assertEqual(self.team_1.points, 0)

    def test_games(self):
        self.assertEqual(self.team_1.games.count(), 0)


# Attribute model
class AttributeModelTest(UnitTestCase):
    def test_init(self):
        attribute = Attribute(
            name='Test Name',
            value='100',
            description='Test description',
            game=self.game
        )
        self.assertEqual(attribute.name, "Test Name")
        self.assertEqual(attribute.value, "100")
        self.assertEqual(attribute.description, "Test description")
        self.assertEqual(attribute.game, self.game)


# Score Modification model
class ScoreModificationModelTest(UnitTestCase):
    def test_init_positive_value(self):
        score_modification = ScoreModification(
            value=100,
            game=self.game,
            reason="Example reason",
            priority=1
        )
        self.assertEqual(score_modification.value, 100)
        self.assertEqual(score_modification.reason, 'Example reason')
        self.assertEqual(score_modification.game, self.game)

    def test_init_negative_value(self):
        score_modification = ScoreModification(
            value=-100,
            game=self.game,
            reason="Example reason",
            priority=1
        )
        self.assertEqual(score_modification.value, -100)
        self.assertEqual(score_modification.reason, 'Example reason')
        self.assertEqual(score_modification.game, self.game)
