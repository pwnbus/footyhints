from sqlalchemy.ext.declarative.api import DeclarativeMeta
from footyhints.models.base import Base


class TestBase(object):

    def test_base_class(self):
        assert isinstance(Base, DeclarativeMeta)
