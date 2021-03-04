import os
import copy
from pytest import raises

from footyhints.config_parser import ConfigParser


class NoEnvironment():
    def delete_env_key(self, keyname):
        if keyname in os.environ:
            del os.environ[keyname]

    def setup(self):
        self.old_environ = copy.deepcopy(os.environ)
        self.delete_env_key("FOOTYHINTS_MODE")
        self.delete_env_key("FOOTYHINTS_API_KEY")
        self.delete_env_key("FOOTYHINTS_WEB_DEBUG")
        self.delete_env_key("FOOTYHINTS_DB_URI")
        self.delete_env_key("FOOTYHINTS_FETCH_LEAGUE_COUNTRY")
        self.delete_env_key("FOOTYHINTS_FETCH_LEAGUE_NAME")
        self.delete_env_key("FOOTYHINTS_CACHE_ENABLED")
        self.delete_env_key("FOOTYHINTS_CACHE_URI")
        self.delete_env_key("FOOTYHINTS_CACHE_EXPIRATION")

    def teardown(self):
        os.environ = self.old_environ


class TestSample1Config(NoEnvironment):
    def setup(self):
        super().setup()
        self.config = ConfigParser(location="../tests/footyhints/example_configs/config1.yml")

    def test_mode(self):
        assert self.config.mode == "development"

    def test_api_key(self):
        assert self.config.api_key is None

    def test_db_uri(self):
        assert self.config.db_uri == "sqlite:///:memory:"

    def test_web_debug(self):
        assert self.config.web_debug is True

    def test_fetch_league_country(self):
        assert self.config.fetch_league_country == 'United States'

    def test_fetch_league_name(self):
        assert self.config.fetch_league_name == 'Premier League'

    def test_cache_enabled(self):
        assert self.config.cache_enabled is False


class TestSample2Config(NoEnvironment):
    def setup(self):
        super().setup()
        self.config = ConfigParser(location="../tests/footyhints/example_configs/config2.yml")

    def test_mode(self):
        assert self.config.mode == "production"

    def test_api_key(self):
        assert self.config.api_key == '12345678'

    def test_google_analytics_api_key(self):
        assert self.config.google_analytics_key == 'test'

    def test_db_uri(self):
        assert self.config.db_uri == "mysql://user:pass@127.0.0.1/footyhints"

    def test_web_debug(self):
        assert self.config.web_debug is False

    def test_fetch_league_country(self):
        assert self.config.fetch_league_country == 'United States'

    def test_fetch_league_name(self):
        assert self.config.fetch_league_name == 'MLS'

    def test_cache_enabled(self):
        assert self.config.cache_enabled is True

    def test_cache_uri(self):
        assert self.config.cache_uri == 'redis://127.0.0.1:6379/1'

    def test_cache_expiration(self):
        assert self.config.cache_expiration == 900


class TestNonexistentConfig(NoEnvironment):
    def test_bad_location(self):
        with raises(KeyError) as exception_obj:
            ConfigParser(location="../tests/footyhints/example_configs/abcd.txt")
        assert 'Unable to find FOOTYHINTS_MODE in environment variable or config file at ' in str(exception_obj.value)


class TestSampleEnvironmentConfig():
    def setup(self):
        os.environ["FOOTYHINTS_MODE"] = "production"
        os.environ["FOOTYHINTS_API_KEY"] = "12345678"
        os.environ["FOOTYHINTS_WEB_DEBUG"] = "False"
        os.environ["FOOTYHINTS_DB_URI"] = "sqlite:///:memory:"
        os.environ["FOOTYHINTS_FETCH_LEAGUE_COUNTRY"] = "United States"
        os.environ["FOOTYHINTS_FETCH_LEAGUE_NAME"] = "Premier League"
        self.config = ConfigParser()

    def test_mode(self):
        assert self.config.mode == "production"

    def test_api_key(self):
        assert self.config.api_key == "12345678"

    def test_db_uri(self):
        assert self.config.db_uri == "sqlite:///:memory:"

    def test_web_debug(self):
        assert self.config.web_debug is False

    def test_fetch_league_country(self):
        assert self.config.fetch_league_country == "United States"

    def test_fetch_league_name(self):
        assert self.config.fetch_league_name == "Premier League"
