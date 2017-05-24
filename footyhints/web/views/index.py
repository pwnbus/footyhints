from flask import Blueprint, render_template
from footyhints.models.game import Game

mod = Blueprint('index', __name__)


@mod.route('/')
@mod.route("/index")
def home():
    games = []
    for game in Game.query.all():
        game.worth_watching()
        game_dict = {
            "home_team": game.home_team.name,
            "away_team": game.away_team.name,
            "interest_level": game.interest_level,
        }
        games.append(game_dict)

    return render_template('index.html', games=games)
