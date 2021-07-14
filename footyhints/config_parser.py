import os
import yaml


class ConfigParser(object):

    def __init__(self, location=None):
        if location is None:
            location = "../config.yml"
        self.config_location = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), location))

        self.mode = self.parse_key('mode')

        self.api_key = None
        if self.mode.lower() == 'production':
            try:
                self.api_key = self.parse_key('api_key')
            except KeyError as exception:
                raise exception

        self.cache_enabled = self.parse_key('cache_enabled', bool)
        if self.cache_enabled:
            self.cache_uri = self.parse_key('cache_uri')
        self.cache_expiration = self.parse_key('cache_expiration', int, 900)

        self.db_uri = self.parse_key('db_uri')
        self.secret_key = self.parse_key('secret_key')
        self.web_debug = self.parse_key('web_debug', bool)

    def convert_key(self, value, objtype):
        if objtype == str:
            return str(value)
        elif objtype == int:
            return int(value)
        elif objtype == bool:
            if type(value) == bool:
                return value
            else:
                return bool(value == 'True')

    def parse_key(self, keyname, objtype=str, default=None):
        environment_key = "FOOTYHINTS_{}".format(keyname.upper())
        if environment_key in os.environ:
            return self.convert_key(os.environ[environment_key], objtype)
        else:
            try:
                with open(self.config_location, 'r') as yaml_stream:
                    self.parser = yaml.safe_load(yaml_stream)
                return self.convert_key(self.parser[keyname.lower()], objtype)
            except (KeyError, FileNotFoundError):
                if default is not None:
                    return default
                else:
                    raise KeyError('Unable to find {0} in environment variable or config file at {1}'.format(environment_key, self.config_location))
