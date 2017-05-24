from flask import Blueprint, render_template
from footyhints.models.game import Game

mod = Blueprint('index', __name__)


@mod.route('/')
@mod.route("/index")
def home():
    games = []
    for game in Game.query.all():
        game_dict = {
            "Home Team": game.home_team.name,
            "Away Team": game.away_team.name,
            "Decision": game.worth_watching(),
        }
        games.append(game_dict)

    return render_template('index.html', games=games)
