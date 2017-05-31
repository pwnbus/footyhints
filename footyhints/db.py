from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from footyhints.config import config


class DB(object):
    def __init__(self):
        self.connected = False
        self.db_uri = config.db_uri
        self.engine = create_engine(self.db_uri, convert_unicode=True)

    def connect(self):
        self.connected = True
        self.session = scoped_session(sessionmaker(bind=self.engine))

    def disconnect(self):
        self.engine.dispose()
        self.session.close()
        self.connected = False

    def check_connection(self):
        if not self.connected:
            raise IOError()

    def setup(self):
        self.check_connection()
        from footyhints.models.base import Base
        Base.metadata.create_all(self.engine)

    def destroy(self):
        self.check_connection()
        from footyhints.models.base import Base
        Base.metadata.drop_all(self.engine)

    def save(self, obj):
        self.check_connection()
        self.session.add(obj)
        self.session.commit()


db = DB()
db.connect()
