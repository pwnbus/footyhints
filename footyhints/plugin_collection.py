import pkgutil
import inspect


class PluginCollection():

    def __init__(self, package, parent):
        self.load_plugins(package, parent)

    def load_plugins(self, package, parent):
        self.plugins = []

        imported_package = __import__(package, fromlist=['footyhints'])
        for ff, plugin_name, ispkg in pkgutil.iter_modules(imported_package.__path__, imported_package.__name__ + '.'):
            plugin_module = __import__(plugin_name, fromlist=['plugins'])
            classes = inspect.getmembers(plugin_module, inspect.isclass)
            for (class_name, class_obj) in classes:
                if issubclass(class_obj, parent) and class_obj is not parent:
                    self.plugins.append(class_obj())
