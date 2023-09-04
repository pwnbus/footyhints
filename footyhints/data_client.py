import requests
import json
from dateutil.parser import parse
from datetime import datetime

from footyhints.config import config
from footyhints.logger import logger


class DataClient():

    API_URL = "https://v3.football.api-sports.io"

    def __init__(self):
        logger.debug("Using football.api-sports.io data client")

    def __determine_season_year(self):
        current_date = datetime.now()
        year = current_date.year
        month = current_date.month
        # If it's January - June we gotta change year
        if month >=1 and month <= 6:
            year = year - 1
        return year

    def get_results(self):
        current_season = self.__determine_season_year()
        headers = {
            'x-rapidapi-host': 'v3.football.api-sports.io',
            'x-rapidapi-key': config.api_key,
        }
        logger.info("Querying for fixtures")
        fixtures_resp = requests.get('{0}/fixtures?league=39&season={1}'.format(self.API_URL, current_season), headers=headers)
        if not fixtures_resp.ok:
            raise Exception('{0}: {1}'.format(fixtures_resp.status_code, fixtures_resp.text))
        fixtures_data = json.loads(fixtures_resp.text)
        if 'errors' in fixtures_data and fixtures_data['errors']:
            raise Exception(fixtures_data['errors'])

        all_competitions = {}
        for match in fixtures_data['response']:
            if match['league']['name'] not in all_competitions:
                all_competitions[match['league']['name']] = {
                    "logo_url": match['league']['logo']
                }

        results = {
            "competitions": {}
        }
        for competition_name, competition_data in all_competitions.items():
            teams = {}
            finished_games = []
            upcoming_games = []
            for match in fixtures_data['response']:
                if match['league']['name'] != competition_name:
                    continue
                home_team_name = match['teams']['home']['name']
                if home_team_name not in teams:
                    teams[home_team_name] = {
                        "logo_url": match['teams']['home']['logo']
                    }
                away_team_name = match['teams']['away']['name']
                if away_team_name not in teams:
                    teams[away_team_name] = {
                        "logo_url": match['teams']['away']['logo']
                    }

                game_result = {
                    "home_team": match['teams']['home']['name'],
                    "away_team": match['teams']['away']['name'],
                    "start_time": parse(match['fixture']['date']).timestamp(),
                    "stadium": match['fixture']['venue']['name'],
                    "city": match['fixture']['venue']['city'],
                    "referee": match['fixture']['referee'],
                }
                if match['fixture']['status']['short'] == 'FT':
                    game_result['home_score'] = match['goals']['home']
                    game_result['away_score'] = match['goals']['away']
                    finished_games.append(game_result)
                elif match['fixture']['status']['short'] == 'PST':
                    continue
                else:
                    upcoming_games.append(game_result)
            if competition_name not in results['competitions']:
                results['competitions'][competition_name] = {}
            results['competitions'][competition_name] = {
                "logo_url": competition_data['logo_url'],
                "teams": teams,
                "finished_games": finished_games,
                "upcoming_games": upcoming_games,
            }
        return results
