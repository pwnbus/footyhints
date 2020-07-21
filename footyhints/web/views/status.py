from flask import Blueprint, render_template

from footyhints.models.competition import Competition
from footyhints.db import session

mod = Blueprint('status', __name__)


@mod.route("/status")
def home():
    competition = session.query(Competition).one()
    return render_template(
        'status.html',
        last_updated=competition.last_updated,
    )
