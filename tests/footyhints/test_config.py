from footyhints.config import Config


class TestConfig(object):

    def setup(self):
        self.config = Config(location="../tests/footyhints/example_conf.txt")

    def test_db_uri(self):
        assert self.config.db_uri == "sqlite:///:memory:"
