import sys
import importlib

from playground.import_system.import_metapath_importer.main import (
    UrlModuleLoader,
    UrlPackageLoader,
)
from playground.import_system.import_metapath_importer.main import log
from playground.import_system.import_metapath_importer.main import _get_links


class UrlPathFinder(importlib.abc.PathEntryFinder):
    def __init__(self, baseurl):
        self._links = None
        self._loader = UrlModuleLoader(baseurl)
        self._baseurl = baseurl

    def find_loader(self, fullname: str):
        log.debug("find_loader: %r", fullname)
        parts = fullname.split(".")
        basename = parts[-1]

        # check link cache
        if self._links is None:
            self._links = []
            self._links = _get_links(self._baseurl)

        # check if it's a package
        if basename in self._links:
            log.debug("find_loader: trying package %r", fullname)
            fullurl = self._baseurl + "/" + basename
            # attempt to load the package (which access __init__.py)
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                log.debug("find_loader: package %r loaded", fullname)
            except ImportError as e:
                log.debug("find_loader: %r is a namespace package", fullname)
                loader = None
            return loader, [fullurl]

        # a normal module
        filename = basename + ".py"
        if filename in self._links:
            log.debug("find_loader: module %r found", fullname)
            return self._loader, []
        else:
            log.debug("find_loader: module %r not found", fullname)
            return None, []

    def invalidate_caches(self) -> None:
        log.debug("invalidating link cache")
        self._links = None


_url_path_cache = {}


def handle_url(path):
    if path.startswith(("http://", "https://")):
        log.debug("handle path? %s. [Yes]", path)
        if path in _url_path_cache:
            finder = _url_path_cache[path]
        else:
            finder = UrlPathFinder(path)
            _url_path_cache[path] = finder
        return finder
    else:
        log.debug("handle path? %s. [No]", path)


def install_path_hook():
    sys.path_hooks.append(handle_url)
    sys.path_importer_cache.clear()
    log.debug("installing handle_url")


def remove_path_hook():
    sys.path_hooks.remove(handle_url)
    sys.path_importer_cache.clear()
    log.debug("removing handle_url")


if __name__ == "__main__":
    install_path_hook()
    sys.path.append("http://localhost:15000")
    import fib
    import grok.blah

    print(fib)
    print(fib.__name__)
    print(fib.__file__)

    import inspect

    print(inspect.getsource(fib))
