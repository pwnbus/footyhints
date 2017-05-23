import os

from flask import Flask

from footyhints.web.views import index

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
app.secret_key = os.urandom(128)

app.register_blueprint(index.mod)
