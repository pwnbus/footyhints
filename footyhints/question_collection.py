from footyhints.question import Question
from footyhints.plugin_collection import PluginCollection


class QuestionCollection(PluginCollection):
    def __init__(self, package):
        super().__init__(package, Question)
