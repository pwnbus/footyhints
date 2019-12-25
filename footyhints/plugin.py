LOWEST_PRIORITY = 2


class Plugin(object):
    def score(self, game):
        raise NotImplementedError('Must specify a score function in the plugin')
