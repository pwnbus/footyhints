from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from footyhints.config import config


engine = create_engine(config.db_uri, pool_recycle=0)
session = scoped_session(sessionmaker(bind=engine))
