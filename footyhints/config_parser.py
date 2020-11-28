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

        try:
            self.google_analytics_key = self.parse_key('google_analytics_key')
        except KeyError:
            self.google_analytics_key = None

        self.db_uri = self.parse_key('db_uri')
        self.secret_key = self.parse_key('secret_key')
        self.web_debug = self.parse_key('web_debug', bool)
        self.fetch_league_country = self.parse_key('fetch_league_country')
        self.fetch_league_name = self.parse_key('fetch_league_name')

    def convert_key(self, value, objtype):
        if objtype == str:
            return str(value)
        elif objtype == bool:
            if type(value) == bool:
                return value
            else:
                return bool(value == 'True')

    def parse_key(self, keyname, objtype=str):
        environment_key = "FOOTYHINTS_{}".format(keyname.upper())
        if environment_key in os.environ:
            return self.convert_key(os.environ[environment_key], objtype)
        else:
            if not os.path.isfile(self.config_location):
                raise KeyError('Unable to find {0} in environment variable or config file at {1}'.format(environment_key, self.config_location))
            with open(self.config_location, 'r') as yaml_stream:
                self.parser = yaml.safe_load(yaml_stream)
            return self.convert_key(self.parser[keyname.lower()], objtype)
