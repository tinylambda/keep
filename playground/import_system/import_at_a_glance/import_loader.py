import sys
import types
from typing import Optional, Sequence

from types import ModuleType
from importlib.machinery import ModuleSpec
from importlib.abc import MetaPathFinder, Loader


class Module(ModuleType):
    def __init__(self, name):
        self.x = 1
        self.name = name


class ExampleLoader(Loader):
    def create_module(self, spec: ModuleSpec) -> Optional[ModuleType]:
        return Module(spec.name)

    def exec_module(self, module: ModuleType) -> None:
        module.y = 2


class ExampleFinder(MetaPathFinder):
    def find_spec(
        self, fullname: str, path, target: Optional[types.ModuleType] = ...
    ) -> Optional[ModuleSpec]:
        return ModuleSpec('module', ExampleLoader())


sys.meta_path = [ExampleFinder()]

import module
print(module)
print(module.x, module.y)


