from footyhints.config import config

import requests
import json
from dateutil.parser import parse


class DataClient():

    API_URL = "https://api.football-data.org"

    def get_results(self):
        headers = {
            'X-Auth-Token': config.api_key,
            'X-Response-Control': 'minified'
        }
        competition_resp = requests.get('{0}/v2/competitions/'.format(self.API_URL), headers=headers)
        if not competition_resp.ok:
            raise Exception('{0}: {1}'.format(competition_resp.status_code, competition_resp.text))

        response = json.loads(competition_resp.text)

        if 'error' in response:
            raise Exception(response['error'])

        competition_id = ""
        for competition in response['competitions']:
            if not competition['name'] == config.fetch_league_name or not competition['area']['name'] == config.fetch_league_country:
                continue
            competition_id = competition['id']

        matches_resp = requests.get('{0}/v2/competitions/{1}/matches?status=FINISHED'.format(self.API_URL, competition_id), headers=headers)
        if not matches_resp.ok:
            raise Exception('{0}: {1}'.format(matches_resp.status_code, matches_resp.text))

        response = json.loads(matches_resp.text)

        results = []
        for match in response['matches']:
            if not match['status'] == 'FINISHED':
                continue

            match_day = match['matchday']
            results.append({
                "home_team": match['homeTeam']['name'],
                "away_team": match['awayTeam']['name'],
                "home_score": match['score']['fullTime']['homeTeam'],
                "away_score": match['score']['fullTime']['awayTeam'],
                "match_day": match_day,
                "start_time": parse(match['utcDate']).timestamp()
            })
        return results
