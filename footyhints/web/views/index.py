from flask import Blueprint

from footyhints.web.render_view import render_view
from footyhints.db import session
from footyhints.models.game import Game

mod = Blueprint('index', __name__)


@mod.route('/')
@mod.route("/index")
def home():
    games = session.query(Game).all()
    return render_view(
        'index.html',
        games=games,
    )
