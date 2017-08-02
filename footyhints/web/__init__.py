import os

from flask import Flask

from footyhints.config import config

from footyhints.web.views import index, api, team

app = Flask(__name__)
app.config['DEBUG'] = config.web_debug
app.secret_key = os.urandom(128)

app.register_blueprint(index.mod)
app.register_blueprint(api.mod)
app.register_blueprint(team.mod)
