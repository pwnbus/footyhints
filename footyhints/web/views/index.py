from flask import Blueprint, render_template
from footyhints.models.game import Game

mod = Blueprint('index', __name__)


@mod.route('/')
@mod.route("/index")
def home():
    games = Game.query.all()
    return render_template('index.html', games=games)
