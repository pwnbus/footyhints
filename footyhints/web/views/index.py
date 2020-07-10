from flask import Blueprint, render_template

from footyhints.db import session
from footyhints.web.utilities.footer import version
from footyhints.models.game import Game

from footyhints.config import config

mod = Blueprint('index', __name__)


@mod.route('/')
@mod.route("/index")
def home():
    games = session.query(Game).all()
    return render_template(
        'index.html',
        games=games,
        league_country=config.fetch_league_country,
        league_name=config.fetch_league_name,
        version=version
    )
