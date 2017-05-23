class Team(object):
    def __init__(self, name):
        if type(name) is not str:
            raise ValueError('Team name must be a string')
        self.name = name
