from flask.blueprints import Blueprint

from footyhints.web import app


class TestInit(object):

    def test_app_config_debug(self):
        assert type(app.config['DEBUG']) is bool

    def test_app_secret_key(self):
        assert type(app.secret_key) is bytes
        assert len(app.secret_key) is 128

    def test_app_blueprints(self):
        expected_blueprints = ['index']

        for blueprint_name in expected_blueprints:
            app_blueprint = app.blueprints[blueprint_name]
            assert type(app_blueprint) is Blueprint
