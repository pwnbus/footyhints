from random import randint, shuffle
import datetime
from footyhints.logger import logger


class SampleDataClient():
    def __init__(self):
        logger.debug("Using sample data client")

    def get_results(self):
        teams = [
            'Arsenal',
            'Aston Villa',
            'Brighton',
            'Burnley',
            'Chelsea',
            'Crystal Palace',
            'Everton',
            'Fulham',
            'Leeds',
            'Leicester',
            'Liverpool',
            'Manchester City',
            'Manchester United',
            'Newcastle',
            'Sheffield Utd',
            'Southampton',
            'Tottenham',
            'West Brom',
            'West Ham',
            'Wolves',
        ]
        results = []
        # Generate finished games
        finished_games = []
        num_match_days = randint(5, 38)
        start_date_pointer = datetime.datetime.now() - datetime.timedelta(days=120)
        for match_day in range(1, num_match_days + 1):
            temp_team_names = [team[:] for team in teams]
            shuffle(temp_team_names)
            while len(temp_team_names) != 0:
                start_time = start_date_pointer + datetime.timedelta(hours=12)
                start_date_pointer = start_time
                home_team = temp_team_names.pop()
                away_team = temp_team_names.pop()
                finished_games.append({
                    'home_score': randint(0, randint(0, 7)),
                    'away_score': randint(0, randint(0, 7)),
                    'home_team': home_team,
                    'away_team': away_team,
                    'city': 'London',
                    'referee': 'H. Webb',
                    'stadium': 'Wembley',
                    'start_time': start_time.timestamp()
                })

        # Generate upcoming games
        upcoming_games = []
        num_match_days = randint(5, 10)
        start_date_pointer = datetime.datetime.now() + datetime.timedelta(days=3)
        for match_day in range(1, num_match_days + 1):
            temp_team_names = [team[:] for team in teams]
            shuffle(temp_team_names)
            while len(temp_team_names) != 0:
                start_time = start_date_pointer + datetime.timedelta(hours=12)
                start_date_pointer = start_time
                home_team = temp_team_names.pop()
                away_team = temp_team_names.pop()
                upcoming_games.append({
                    'home_team': home_team,
                    'away_team': away_team,
                    'city': 'London',
                    'referee': 'H. Webb',
                    'stadium': 'Wembley',
                    'start_time': start_time.timestamp()
                })

        teams_data = {}
        for team in teams:
            teams_data[team] = {
                "logo_url": None
            }

        results = {
            'competitions': {
                'Premier League': {
                    'finished_games': finished_games,
                    'logo_url': None,
                    'teams': teams_data,
                    'upcoming_games': upcoming_games,
                }
            }
        }

        return results
