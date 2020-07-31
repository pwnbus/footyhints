from os import environ

from flask import render_template

from footyhints.db import session
from footyhints.models.game import Game
from footyhints.models.team import Team
from footyhints.models.competition import Competition

from footyhints.config import config


def render_view(template_name, **kwargs):
    version = 'v.dev'
    if 'FOOTYHINTS_VERSION' in environ:
        version = environ.get('FOOTYHINTS_VERSION')

    teams = session.query(Team).order_by(Team.name.asc()).all()

    competition = session.query(Competition).one()

    global_args = {
        "template_name_or_list": template_name,
        "teams": teams,
        "league_country": config.fetch_league_country,
        "league_name": config.fetch_league_name,
        "version": version,
        "last_updated": competition.last_updated,
    }
    final_args = {**kwargs, **global_args}
    return render_template(**final_args)
