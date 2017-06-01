from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.orm import Session

from footyhints.config import config


engine = create_engine(config.db_uri)
session = scoped_session(sessionmaker(bind=engine))
