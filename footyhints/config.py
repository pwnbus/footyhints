import configparser
import os


class Config(object):

    def __init__(self, location=None):
        if location is None:
            location = "../config.txt"
        config_location = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), location))

        if not os.path.isfile(config_location):
            raise RuntimeError('Unable to find config file at ' + config_location)
        self.parser = configparser.ConfigParser()
        self.parser.read(config_location)

        self.db_uri = self.parser['DB']['uri']
        self.web_debug = self.parser['WEB']['debug'] == 'True'
        self.fetch_season_name = self.parser['FETCH']['season_name']


config = Config()
