import os

from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
app.secret_key = os.urandom(128)

from footyhints.web.views import index

app.register_blueprint(index.mod)
