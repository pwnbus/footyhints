from footyhints.db import engine, session
from footyhints.models.team import Team

from tests.footyhints.unit_test import UnitTest


class TestDB(UnitTest):

    def test_engine(self):
        assert str(engine.url) == 'sqlite:////tmp/footyhints.db'
        assert len(engine.table_names()) > 0

    def test_session(self):
        assert session.is_active is True

    def test_save_and_delete(self):
        obj = Team(name="Chelsea")
        session.add(obj)
        session.commit()
        assert len(session.query(Team).all()) == 1
        session.delete(obj)
        session.commit()
        assert len(session.query(Team).all()) == 0
