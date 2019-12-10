from footyhints.config import config

import http.client
import json


class DataClient():

    def get_results(self):
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = {
            'X-Auth-Token': config.api_key,
            'X-Response-Control': 'minified'
        }
        connection.request('GET', '/v2/competitions/', None, headers)
        response = json.loads(connection.getresponse().read().decode())

        if 'error' in response:
            raise Exception(response['error'])

        competition_id = ""
        for competition in response['competitions']:
            if not competition['name'] == config.fetch_league_name or not competition['area']['name'] == config.fetch_league_country:
                continue
            competition_id = competition['id']

        connection.request('GET', "/v2/competitions/{}/matches".format(competition_id), None, headers)
        response = json.loads(connection.getresponse().read().decode())

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
                "match_day": match_day
            })
        return results
