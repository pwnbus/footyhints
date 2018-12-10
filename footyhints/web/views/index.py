from flask import Blueprint, render_template
from footyhints.config import config

mod = Blueprint('index', __name__)


@mod.route('/')
@mod.route("/index")
def home():
    return render_template(
        'index.html',
        league_country=config.fetch_league_country,
        league_name=config.fetch_league_name
    )
