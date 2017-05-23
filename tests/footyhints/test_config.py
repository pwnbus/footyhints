from footyhints.config import Config


class TestSample1Config(object):
    def setup(self):
        self.config = Config(location="../tests/footyhints/example_configs/config1.txt")

    def test_db_uri(self):
        assert self.config.db_uri == "sqlite:///:memory:"

    def test_web_debug(self):
        assert self.config.web_debug is True


class TestSample2Config(object):
    def setup(self):
        self.config = Config(location="../tests/footyhints/example_configs/config2.txt")

    def test_db_uri(self):
        assert self.config.db_uri == "mysql://user:pass@127.0.0.1/footyhints"

    def test_web_debug(self):
        assert self.config.web_debug is False
