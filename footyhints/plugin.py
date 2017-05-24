class Plugin(object):
    def __init__(self, game):
        self.game = game

    def score(self):
        raise NotImplementedError('Must specify a score function in plugin')
