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

    def set_score(self, home_team_score, away_team_score):
        if type(home_team_score) is not int and type(away_team_score) is not int:
            raise ValueError('Home and away scores must be integers')
        elif type(home_team_score) is not int:
            raise ValueError('Home team score must be an integer')
        elif type(away_team_score) is not int:
            raise ValueError('Away team score must be an integer')

        self.home_score = home_team_score
        self.away_score = away_team_score

    def __validate_score(self):
        # Check if team scores have been set in the game
        if self.home_score is None and self.away_score is None:
            raise ValueError('Score must be defined for both the home and away team')

    def worth_watching(self):
        self.__validate_score()
        # Main decision logic

        #   If score is 0 0, not worth watching
        if self.home_score == 0 and self.away_score == 0:
            return False

        return True
