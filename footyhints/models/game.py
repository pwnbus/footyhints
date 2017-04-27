from footyhints.models.team import Team


class Game(object):
    def __init__(self, home_team, away_team):
        if not type(home_team) is Team:
            raise ValueError('home_team must be of type "Team"')
        if not type(away_team) is Team:
            raise ValueError('away_team must be of type "Team"')

        self.home_team = home_team
        self.away_team = away_team
