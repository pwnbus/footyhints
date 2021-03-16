from glob import glob
from os.path import join, dirname, abspath

from footyhints.score_collection import ScoreCollection

from tests.footyhints.unit_test import UnitTest


class TestScoreCollection(UnitTest):

    def test_plugins(self):
        plugin_collection = ScoreCollection('footyhints.score_plugins')
        plugins_path = join(dirname(abspath(__file__)), '../../footyhints/score_plugins')
        expected_plugin_num = len(glob(plugins_path + "/*.py")) - 1
        assert len(plugin_collection.plugins) == expected_plugin_num
