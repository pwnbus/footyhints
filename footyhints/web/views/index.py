from flask import Blueprint, render_template
from footyhints.db import session
from footyhints.models.game import Game

mod = Blueprint('index', __name__)


@mod.route('/')
@mod.route("/index")
def home():
    games = []
    for game in session.query(Game).all():
        game.worth_watching()
        games.append(game)

    return render_template('index.html', games=games)
