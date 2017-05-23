from sqlalchemy.orm import scoped_session
from sqlalchemy.exc import OperationalError

from footyhints.db import DB
from footyhints.models.team import Team

import pytest


class TestDB(object):

    def setup(self):
        self.db = DB()
        try:
            self.db.destroy()
        except IOError:
            pass

    def teardown(self):
        try:
            self.db.destroy()
        except IOError:
            pass

    def test_init(self):
        assert self.db.connected is False

    def test_connect_without_setup(self):
        self.db.connect()
        assert self.db.connected is True
        assert isinstance(self.db.session, scoped_session) is True

    def test_connect_disconnect(self):
        assert self.db.connected is False
        self.db.connect()
        assert self.db.connected is True
        self.db.disconnect()
        assert self.db.connected is False

    def test_setup_without_connecting(self):
        with pytest.raises(IOError):
            self.db.setup()

    def test_save_without_connecting(self):
        obj = Team(name="Chelsea")
        with pytest.raises(IOError):
            self.db.save(obj)

    def test_save_and_destroy(self):
        self.db.connect()
        self.db.setup()
        obj = Team(name="Chelsea")
        self.db.save(obj)
        assert len(Team.query.all()) == 1
        self.db.destroy()
        with pytest.raises(OperationalError):
            Team.query.all()
