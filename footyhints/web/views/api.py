from flask import Blueprint, jsonify
from footyhints.db import session
from footyhints.models.game import Game

mod = Blueprint('api', __name__)


@mod.route('/api/games')
def api_games():
    data = []
    for game in session.query(Game).all():
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
    return jsonify(data=data)
