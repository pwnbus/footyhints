from sqlalchemy.ext.declarative import declarative_base

from footyhints.db import db

Base = declarative_base()
Base.query = db.session.query_property()
