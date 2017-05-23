from pytest import raises

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


class TestNonexistentConfig(object):
    def test_bad_location(self):
        with raises(RuntimeError) as exception_obj:
            Config(location="../tests/footyhints/example_configs/abcd.txt")
        assert 'Unable to find config file at' in str(exception_obj.value)
