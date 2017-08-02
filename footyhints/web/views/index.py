from flask import Blueprint, render_template
from footyhints.config import config

mod = Blueprint('index', __name__)


@mod.route('/')
@mod.route("/index")
def home():
    return render_template('index.html', season_name=config.fetch_season_name)
