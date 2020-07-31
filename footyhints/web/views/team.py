from flask import Blueprint, render_template, redirect

from footyhints.db import session
from footyhints.web.utilities.footer import version
from footyhints.config import config
from footyhints.models.team import Team

mod = Blueprint('team', __name__)


@mod.route('/team/<id>')
def team(id):
    team = session.query(Team).get(id)
    if team is None:
        return redirect("/"), 404

    teams = session.query(Team).order_by(Team.name.asc()).all()
    return render_template(
        'team.html',
        team=team,
        teams=teams,
        league_country=config.fetch_league_country,
        league_name=config.fetch_league_name,
        version=version
    )
