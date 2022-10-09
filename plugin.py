import os


class Plugins:

    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir

    def load_plugins(self):
        plugins = []
        if self.plugin_dir is None:
            return plugins
        for file_name in os.listdir(self.plugin_dir):
            if not file_name.startswith("__") and file_name.endswith(".py"):
                module_name = file_name.split(".")[0]
                plugins.append(__import__(self.plugin_dir + "." + module_name, fromlist=[file_name]))
        return plugins
