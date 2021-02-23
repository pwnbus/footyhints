from django.db import models
from time import time
from datetime import datetime


class Competition(models.Model):
    name = models.TextField(null=False)
    last_updated = models.IntegerField(null=True)
    games = models.ManyToManyField('Game')
    teams = models.ManyToManyField('Team')
    logo_image = models.ImageField('img', upload_to='web/static/images/dynamic/competitions', default='web/static/images/default_competition_logo.png')

    @property
    def logo(self):
        return "/" + self.logo_image.name.replace("web/", "")

    def update_timestamp(self):
        self.last_updated = int(time())


class Team(models.Model):
    name = models.TextField(null=False)
    points = models.IntegerField(default=0)
    place = models.IntegerField(default=0)
    games = models.ManyToManyField('Game')
    logo_image = models.ImageField('img', upload_to='web/static/images/dynamic/teams', default='web/static/images/default_team_logo.png')

    @property
    def logo(self):
        return "/" + self.logo_image.name.replace("web/", "")

    @property
    def goals_info(self):
        num_goals_for = 0
        num_goals_against = 0
        for game in self.games.filter(finished=True):
            if game.home_team == self:
                num_goals_for += game.home_team_score
                num_goals_against += game.away_team_score
            elif game.away_team == self:
                num_goals_against += game.home_team_score
                num_goals_for += game.away_team_score
        return {
            "goals_for": num_goals_for,
            "goals_against": num_goals_against,
            "goal_difference": num_goals_for - num_goals_against
        }

    @property
    def games_info(self):
        num_played = 0
        num_wins = 0
        num_draws = 0
        num_loses = 0
        for game in self.games.filter(finished=True):
            num_played += 1
            if game.home_team == self:
                if game.home_team_score > game.away_team_score:
                    num_wins += 1
                elif game.home_team_score == game.away_team_score:
                    num_draws += 1
                else:
                    num_loses += 1
            elif game.away_team == self:
                if game.away_team_score > game.home_team_score:
                    num_wins += 1
                elif game.away_team_score == game.home_team_score:
                    num_draws += 1
                else:
                    num_loses += 1
        return {
            "played": num_played,
            "wins": num_wins,
            "draws": num_draws,
            "loses": num_loses,
        }

    def __lt__(self, other):
        if self.points == other.points:
            # Go to goal difference as tie breaker
            return self.goals_info['goal_difference'] < other.goals_info['goal_difference']
        else:
            return self.points < other.points


class Game(models.Model):
    start_time = models.IntegerField(null=False)
    finished = models.BooleanField(default=False)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_team_games")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_team_games")
    interest_score = models.FloatField(null=True)
    interest_level = models.TextField(null=True)
    attributes = models.ManyToManyField('Attribute')
    score_modifications = models.ManyToManyField('ScoreModification')
    stadium = models.TextField(null=True)
    city = models.TextField(null=True)
    referee = models.TextField(null=True)

    @property
    def sorted_score_modifications(self):
        return self.score_modifications.all().order_by('priority')

    def get_attribute_by_name(self, name):
        for attribute in self.attributes.all():
            if attribute.name == name:
                attribute_value = attribute.value
                if attribute_value:
                    return attribute_value

    def __str__(self):
        return "{0} vs {1} start_time={2} interest_score={3} interest_level={4}".format(
            self.home_team.name,
            self.away_team.name,
            self.start_time,
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
        self.finished = True
        self.save()

    def __eq__(self, other):
        if isinstance(other, Game):
            return self.id == other.id and self.start_time == other.start_time and self.home_team.name == other.home_team.name and self.away_team.name == other.away_team.name
        return False


class Attribute(models.Model):
    name = models.TextField()
    value = models.TextField()
    description = models.TextField()


class ScoreModification(models.Model):
    value = models.IntegerField()
    priority = models.IntegerField()
    reason = models.TextField()
