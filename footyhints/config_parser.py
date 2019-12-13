import configparser
import os


class ConfigParser(object):

    def __init__(self, location=None):
        if location is None:
            location = "../config.txt"
        self.config_location = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), location))

        self.mode = self.parse_key('mode')

        self.api_key = None
        if self.mode.lower() == 'production':
            self.api_key = self.parse_key('api_key')

        self.db_uri = self.parse_key('db_uri')
        self.web_debug = self.parse_key('web_debug', bool)
        self.fetch_league_country = self.parse_key('fetch_league_country')
        self.fetch_league_name = self.parse_key('fetch_league_name')

    def convert_key(self, value, objtype):
        if objtype == str:
            return str(value)
        elif objtype == bool:
            return bool(value == 'True')

    def parse_key(self, keyname, objtype=str):
        environment_key = "FOOTYHINTS_{}".format(keyname.upper())
        if environment_key in os.environ:
            return self.convert_key(os.environ[environment_key], objtype)
        else:
            if not os.path.isfile(self.config_location):
                raise RuntimeError('Unable to find config file at ' + self.config_location)
            self.parser = configparser.ConfigParser()
            self.parser.read(self.config_location)
            return self.convert_key(self.parser['GENERAL'][keyname.lower()], objtype)
