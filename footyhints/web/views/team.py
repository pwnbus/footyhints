from flask import Blueprint, redirect

from footyhints.web.render_view import render_view
from footyhints.db import session
from footyhints.models.team import Team

mod = Blueprint('team', __name__)


@mod.route('/team/<id>')
def team(id):
    team = session.query(Team).get(id)
    if team is None:
        return redirect("/"), 404

    return render_view(
        'team.html',
        team=team,
    )
