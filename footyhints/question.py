

class Question(object):
    def answer(self, game):
        raise NotImplementedError('Must specify an answer function in the plugin')
