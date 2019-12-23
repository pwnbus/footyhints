LOWEST_PRIORITY = 2


class Plugin(object):
    @property
    def description(self):
        raise NotImplementedError('Must specify a description property in the plugin')

    def score(self, game):
        raise NotImplementedError('Must specify a score function in the plugin')
