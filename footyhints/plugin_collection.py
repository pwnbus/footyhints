import pkgutil
import inspect

from footyhints.plugin import Plugin


class PluginCollection():

    def __init__(self, package):
        self.load_plugins(package)

    def load_plugins(self, package):
        self.plugins = []
        imported_package = __import__(package, fromlist=['footyhints'])
        for ff, plugin_name, ispkg in pkgutil.iter_modules(imported_package.__path__, imported_package.__name__ + '.'):
            plugin_module = __import__(plugin_name, fromlist=['plugins'])
            classes = inspect.getmembers(plugin_module, inspect.isclass)
            for (class_name, class_obj) in classes:
                if issubclass(class_obj, Plugin) and class_obj is not Plugin:
                    self.plugins.append(class_obj())
