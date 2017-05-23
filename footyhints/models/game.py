from footyhints.models.team import Team


class Game(object):
    def __init__(self, home_team, away_team):
        if not type(home_team) is Team:
            raise ValueError('home_team must be of type "Team"')
        if not type(away_team) is Team:
            raise ValueError('away_team must be of type "Team"')

        self.home_team = home_team
        self.away_team = away_team
        self.home_score = None
        self.away_score = None

    def worth_watching(self):
        if self.home_score is None and self.away_score is None:
            raise ValueError('Score must be defined for both the home and away team')
        elif self.home_score is None:
            raise ValueError('Score must be defined for the home team')
        elif self.away_score is None:
            raise ValueError('Score must be defined for the away team')

        # Check if home team score exists
        # Check if away team score exists

        # Main decision consists of:
        #   If score is nil nil, not worth watching
