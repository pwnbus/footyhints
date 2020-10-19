from random import randint, shuffle
import datetime
from footyhints.logger import logger


class SampleDataClient():
    def __init__(self):
        logger.debug("Using sample data client")

    def get_results(self):
        teams = [
            'Arsenal FC',
            'Aston Villa FC',
            'Burnley FC',
            'Brighton & Hove Albion FC',
            'Chelsea FC',
            'Crystal Palace FC',
            'Everton FC',
            'Fulham FC',
            'Leicester City FC',
            'Leeds United FC',
            'Liverpool FC',
            'Manchester City FC',
            'Manchester United FC',
            'Newcastle United FC',
            'Sheffield United FC',
            'Southampton FC',
            'Tottenham Hotspur FC',
            'West Bromwich Albion FC',
            'West Ham United FC',
            'Wolverhampton Wanderers FC',
        ]
        results = []
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
                results.append({
                    "home_team": home_team,
                    "away_team": away_team,
                    "home_score": randint(0, randint(0, 7)),
                    "away_score": randint(0, randint(0, 7)),
                    "match_day": match_day,
                    "start_time": start_time.timestamp()
                })

        return results
