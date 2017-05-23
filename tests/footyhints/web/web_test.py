import importlib
from flask import render_template as render_template_orig
from flask.testing import FlaskClient as BaseFlaskClient
from mock import MagicMock, call

from footyhints.web import app


class WebTest(object):

    def setup(self):
        self.app = app
        self.app.test_client_class = BaseFlaskClient
        self.client = self.app.test_client()
        view_name = self.__class__.__name__[4:]
        self.view_module = importlib.import_module('footyhints.web.views.' + view_name.lower(), '*')
        self.view_module.render_template = MagicMock()
        self.mock_obj = self.view_module.render_template
        self.mock_obj.side_effect = lambda *args, **kwargs: render_template_orig(*args, **kwargs)

    def build_args(self, *args, **kwargs):
        return call(*args, **kwargs)

    def test_debug(self):
        assert self.app.debug is True