import sys

from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec


class NoSuchModuleFinder(MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        return ModuleSpec("nosuchmodule", None)


sys.meta_path = [NoSuchModuleFinder()]

import nosuchmodule
