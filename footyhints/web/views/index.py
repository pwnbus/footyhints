from flask import Blueprint, render_template
from footyhints.db import session
from footyhints.models.game import Game
from footyhints.config import config

mod = Blueprint('index', __name__)


@mod.route('/')
@mod.route("/index")
def home():
    games = []
    for game in session.query(Game).all():
        games.append(game)

    return render_template('index.html', games=games, season_name=config.fetch_season_name)
