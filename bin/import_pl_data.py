from footyhints.models.team import Team
from footyhints.models.round import Round
from footyhints.models.game import Game

from footyhints.config import config
from footyhints.db import session, create_db, delete_db

import http.client
import json
from sys import exit


def import_production_data():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {
        'X-Auth-Token': config.api_key,
        'X-Response-Control': 'minified'
    }
    connection.request('GET', '/v2/competitions/', None, headers)
    response = json.loads(connection.getresponse().read().decode())

    if 'error' in response:
        print(response['error'])
        exit(1)

    competition_id = ""
    for competition in response['competitions']:
        if not competition['name'] == config.fetch_league_name or not competition['area']['name'] == config.fetch_league_country:
            continue
        competition_id = competition['id']

    connection.request('GET', "/v2/competitions/{}/teams".format(competition_id), None, headers)
    response = json.loads(connection.getresponse().read().decode())
    teams = {}
    for team_dict in response['teams']:
        name = team_dict['name']
        team = Team(name=name)
        teams[name] = team

    connection.request('GET', "/v2/competitions/{}/matches".format(competition_id), None, headers)
    response = json.loads(connection.getresponse().read().decode())

    rounds = []
    for match in response['matches']:
        if not match['status'] == 'FINISHED':
            continue

        round_num = match['matchday']
        round_obj = None
        for tmp_round in rounds:
            if round_num == tmp_round.num:
                round_obj = tmp_round

        if round_obj is None:
            round_obj = Round(round_num)
            rounds.append(round_obj)
            session.add(round_obj)
        home_team_name = match['homeTeam']['name']
        away_team_name = match['awayTeam']['name']
        home_team_score = match['score']['fullTime']['homeTeam']
        away_team_score = match['score']['fullTime']['awayTeam']

        home_team = teams[home_team_name]
        away_team = teams[away_team_name]
        game = Game(home_team=home_team, away_team=away_team, round=round_obj)
        game.set_score(home_team_score, away_team_score)
        print("Creating game\t{0} | {1}\t{2}-{3} ({4})".format(
            home_team_name,
            away_team_name,
            game.home_team_score,
            game.away_team_score,
            round_obj.num
        ))
        game.worth_watching()
        session.add(game)
    session.commit()
    session.close()


if __name__ == '__main__':
    if config.mode != 'production':
        print("Mode must be 'production'")
        exit(1)
    if config.api_key is None:
        print("Must specify the 'api_key' value in the config")
        exit(1)

    print("Setting up DB")
    delete_db()
    create_db()
    import_production_data()
