from flask import Blueprint, jsonify
from footyhints.db import session
from footyhints.models.game import Game
from footyhints.models.team import Team

mod = Blueprint('api', __name__)


@mod.route('/api/games/all')
def api_games_all():
    data = []
    games = session.query(Game).all()
    data = generate_games_data(games)
    return jsonify(data=data)


def generate_games_data(games):
    data = []
    for game in games:
        score_modifications = []
        for score_modification in game.score_modifications:
            score_modifications.append([score_modification.value, score_modification.description])

        data.append(dict(
            game_id=game.id,
            home_team=game.home_team.name,
            away_team=game.away_team.name,
            round_num=game.round.num,
            interest_level=game.interest_level,
            interest_score=game.interest_score,
            score_modifications=score_modifications
        ))
    return data


@mod.route('/api/team/<id>/games')
def api_team_games(id):
    team = session.query(Team).get(id)
    data = generate_games_data(team.games)
    return jsonify(data=data)
