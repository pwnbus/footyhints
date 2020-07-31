import importlib
from flask import render_template as render_template_orig
from flask.testing import FlaskClient as BaseFlaskClient
from mock import MagicMock, call

from footyhints.web import app

from tests.footyhints.unit_test import UnitTest


class WebTest(UnitTest):

    def setup(self):
        super().setup()
        self.app = app
        self.app.test_client_class = BaseFlaskClient
        self.client = self.app.test_client()
        view_name = self.__class__.__name__[4:]
        self.view_module = importlib.import_module('footyhints.web.views.' + view_name.lower(), '*')
        self.view_module.render_view = MagicMock()
        self.mock_obj = self.view_module.render_view
        self.mock_obj.side_effect = lambda *args, **kwargs: render_template_orig(*args, **kwargs)

        self.session.add(self.home_team)
        self.session.add(self.away_team)
        self.session.commit()
        self.game.set_score(3, 3)
        self.session.add(self.game)
        self.session.commit()

    def build_args(self, *args, **kwargs):
        return call(*args, **kwargs)
