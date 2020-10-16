from glob import glob
from os.path import join, dirname, abspath

from footyhints.plugin_collection import PluginCollection

from tests.footyhints.unit_test import UnitTest


class TestPluginCollection(UnitTest):

    def test_plugins(self):
        plugin_collection = PluginCollection('footyhints.plugins')
        plugins_path = join(dirname(abspath(__file__)), '../../footyhints/plugins')
        expected_plugin_num = len(glob(plugins_path + "/*.py")) - 1
        assert len(plugin_collection.plugins) == expected_plugin_num
