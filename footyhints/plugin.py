class Plugin(object):
    def __init__(self, game):
        self.game = game

    def decision(self):
        raise NotImplementedError('Must specify a decision function in plugin')
