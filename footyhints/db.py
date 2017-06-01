from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker

from footyhints.config import config
from footyhints.models.base import Base

engine = create_engine(config.db_uri)
session = scoped_session(sessionmaker(bind=engine))


def create_db():
    Base.metadata.create_all(engine)


def delete_db():
    Base.metadata.drop_all(engine)
