import requests
import json
from dateutil.parser import parse

from footyhints.config import config
from footyhints.logger import logger


class DataClient():

    API_URL = "https://v3.football.api-sports.io"

    def __init__(self):
        logger.debug("Using football.api-sports.io data client")

    def get_results(self):
        headers = {
            'x-rapidapi-host': 'v3.football.api-sports.io',
            'x-rapidapi-key': config.api_key,
        }
        logger.debug("Querying for fixtures")
        fixtures_resp = requests.get('{0}/fixtures?league=39&season=2020'.format(self.API_URL), headers=headers)
        if not fixtures_resp.ok:
            raise Exception('{0}: {1}'.format(fixtures_resp.status_code, fixtures_resp.text))
        fixtures_data = json.loads(fixtures_resp.text)
        if 'errors' in fixtures_data and fixtures_data['errors']:
            raise Exception(fixtures_data['errors'])

        results = []
        unfinished_matches = []
        for match in fixtures_data['response']:
            if match['fixture']['status']['short'] != 'FT':
                if match['fixture']['status']['short'] != 'PST':
                    unfinished_matches.append(match)
                continue

            results.append({
                "home_team": match['teams']['home']['name'],
                "away_team": match['teams']['away']['name'],
                "home_score": match['goals']['home'],
                "away_score": match['goals']['away'],
                "start_time": parse(match['fixture']['date']).timestamp(),
                "finished": True,
            })

        # Add next 10 games as upcoming
        for match in sorted(unfinished_matches, key=lambda match: match['fixture']['date']):
            results.append({
                "home_team": match['teams']['home']['name'],
                "away_team": match['teams']['away']['name'],
                "start_time": parse(match['fixture']['date']).timestamp(),
                "finished": False,
            })
        return results
