from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from footyhints.config import config


class DB(object):
    def __init__(self):
        self.connected = False
        self.db_uri = config.db_uri

    def connect(self):
        self.connected = True
        self.engine = create_engine(self.db_uri, convert_unicode=True)
        self.session = scoped_session(sessionmaker(bind=self.engine))

    def setup(self):
        if not self.connected:
            raise IOError()

        from footyhints.models.team import Team
        from footyhints.models.game import Game
        from footyhints.models.base import Base
        Base.metadata.create_all(self.engine)

    def destroy(self):
        if not self.connected:
            raise IOError()
        from footyhints.models.team import Team
        from footyhints.models.game import Game
        from footyhints.models.base import Base
        Base.metadata.drop_all(self.engine)

    def save(self, obj):
        if not self.connected:
            raise IOError()

        self.session.add(obj)
        self.session.commit()

    def disconnect(self):
        self.engine.dispose()
        self.session.close()


db = DB()
db.connect()
