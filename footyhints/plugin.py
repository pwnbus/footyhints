class Plugin(object):
    def __init__(self, game):
        self.game = game

    @property
    def max_score(self):
        raise NotImplementedError('Must specify a max_score property in the plugin')

    @property
    def description(self):
        raise NotImplementedError('Must specify a description property in the plugin')

    def score(self):
        raise NotImplementedError('Must specify a score function in the plugin')
