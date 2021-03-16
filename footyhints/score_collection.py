from footyhints.score_plugin import ScorePlugin
from footyhints.plugin_collection import PluginCollection


class ScoreCollection(PluginCollection):
    def __init__(self, package):
        super().__init__(package, ScorePlugin)
