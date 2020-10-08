from django.db import models
from time import time
from datetime import datetime


class Competition(models.Model):
    name = models.TextField(null=False)
    last_updated = models.IntegerField(null=True)
    games = models.ManyToManyField('Game')
    teams = models.ManyToManyField('Team')

    def update_timestamp(self):
        self.last_updated = int(time())


class Team(models.Model):
    name = models.TextField(null=False)
    points = models.IntegerField(default=0)
    games = models.ManyToManyField('Game')


class Game(models.Model):
    match_day = models.IntegerField()
    start_time = models.IntegerField(null=False)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_team_games")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_team_games")
    interest_score = models.FloatField(null=True)
    interest_level = models.CharField(max_length=30, null=True)
    attributes = models.ManyToManyField('Attribute')
    score_modifications = models.ManyToManyField('ScoreModification')

    def get_attribute_by_name(self, name):
        for attribute in self.attributes.all():
            if attribute.name == name:
                attribute_value = attribute.value
                if attribute_value:
                    return attribute_value

    def __str__(self):
        return "{0} vs {1} match_day={2} interest_score={3} interest_level={4}".format(
            self.home_team.name,
            self.away_team.name,
            self.match_day,
            self.interest_score,
            self.interest_level
        )

    @property
    def home_team_score(self):
        return int(self.get_attribute_by_name('home_score'))

    @property
    def away_team_score(self):
        return int(self.get_attribute_by_name('away_score'))

    @property
    def date_from_start_time(self):
        return datetime.fromtimestamp(self.start_time).strftime("%A %d %B %Y")

    def set_score(self, home_team_score, away_team_score):
        if type(home_team_score) is not int and type(away_team_score) is not int:
            raise TypeError('Home and away scores must be integers')
        elif type(home_team_score) is not int:
            raise TypeError('Home team score must be an integer')
        elif type(away_team_score) is not int:
            raise TypeError('Away team score must be an integer')

        if home_team_score > away_team_score:
            self.home_team.points += 3
        elif home_team_score == away_team_score:
            self.home_team.points += 1
            self.away_team.points += 1
        else:
            self.away_team.points += 3

        self.home_team.save()
        self.away_team.save()

        home_score = Attribute(name='home_score', value=str(home_team_score), description='Home Team Score', game=self)
        home_score.save()
        self.attributes.add(home_score)
        away_score = Attribute(name='away_score', value=str(away_team_score), description='Away Team Score', game=self)
        away_score.save()
        self.attributes.add(away_score)
        self.save()

    def __eq__(self, other):
        if isinstance(other, Game):
            return self.id == other.id and self.match_day == other.match_day and self.home_team.name == other.home_team.name and self.away_team.name == other.away_team.name
        return False


class Attribute(models.Model):
    name = models.TextField()
    value = models.TextField()
    description = models.TextField()


class ScoreModification(models.Model):
    value = models.IntegerField()
    priority = models.IntegerField()
    reason = models.TextField()