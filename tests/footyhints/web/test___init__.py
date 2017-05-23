import footyhints.web
from flask.blueprints import Blueprint


class TestInit(object):

    def test_app_config_debug(self):
        assert footyhints.web.app.config['DEBUG'] is True

    def test_app_secret_key(self):
        assert type(footyhints.web.app.secret_key) is bytes
        assert len(footyhints.web.app.secret_key) is 128

    def test_app_blueprints(self):
        expected_blueprints = ['index']

        for blueprint_name in expected_blueprints:
            app_blueprint = footyhints.web.app.blueprints[blueprint_name]
            assert type(app_blueprint) is Blueprint
