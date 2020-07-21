from footyhints.models.base import Base
from footyhints.db import engine


def create_db():
    Base.metadata.create_all(engine)


def delete_db():
    Base.metadata.drop_all(engine)
