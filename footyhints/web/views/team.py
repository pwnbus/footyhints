from flask import Blueprint, render_template, redirect

from footyhints.db import session
from footyhints.config import config
from footyhints.models.team import Team

mod = Blueprint('team', __name__)


@mod.route('/team/<id>')
def team(id):
    team = session.query(Team).get(id)
    if team is None:
        return redirect("/"), 404
    return render_template('team.html', team=team, season_name=config.fetch_season_name)
