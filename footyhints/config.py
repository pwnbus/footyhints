import configparser
import os


class Config(object):

    def __init__(self, location=None):
        if location is None:
            location = "../config.txt"
        config_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), location)

        self.parser = configparser.ConfigParser()
        self.parser.read(config_location)

        self.db_uri = self.parser['DB']['uri']


config = Config()
