import sys
import importlib.abc
import types
from types import ModuleType
from typing import Optional
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser

import logging

log = logging.getLogger(__name__)


def _get_links(url):
    links = set()

    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == "a":
                attrs = dict(attrs)
                links.add(attrs.get("href").rstrip("/"))

    try:
        log.debug("getting links from %s" % url)
        u = urlopen(url)
        parser = LinkParser()
        parser.feed(u.read().decode("utf-8"))
    except Exception as e:
        log.debug("could not get links. %s", e)
    log.debug("links: %r", links)
    return links


class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._links = {}
        self._loaders = {baseurl: UrlModuleLoader(baseurl)}

    def find_module(self, fullname: str, path=None):
        log.debug("find_module: fullname=%r, path=%r", fullname, path)
        if path is None:
            baseurl = self._baseurl
        else:
            if not path[0].startswith(self._baseurl):
                return None
            baseurl = path[0]
        parts = fullname.split(".")
        basename = parts[-1]
        log.debug("find_module: baseurl=%r, basename=%r", baseurl, basename)

        if basename not in self._links:
            self._links[baseurl] = _get_links(baseurl)

        if basename in self._links[baseurl]:
            log.debug("find_module: trying package %r" % fullname)
            fullurl = self._baseurl + "/" + basename
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                self._links[fullurl] = _get_links(fullurl)
                self._loaders[fullurl] = UrlModuleLoader(fullurl)
                log.debug("find_module: package %r loaded", fullname)
            except ImportError as e:
                log.debug("find_module: package failed. %s", e)
                loader = None
            return loader
        filename = basename + ".py"
        if filename in self._links[baseurl]:
            log.debug("find_module: module %r found", fullname)
            return self._loaders[baseurl]
        else:
            log.debug("find_module: module %r not found", fullname)
            return None

    def invalidate_caches(self) -> None:
        log.debug("invalidating link cache")
        self._links.clear()


class UrlModuleLoader(importlib.abc.SourceLoader):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._source_cache = {}

    def module_repr(self, module: ModuleType) -> str:
        return "<urlmodule %r from %r>" % (module.__name__, module.__file__)

    def load_module(self, fullname: str) -> types.ModuleType:
        code = self.get_code(fullname)
        mod = sys.modules.setdefault(fullname, types.ModuleType(fullname))
        mod.__file__ = self.get_filename(fullname)
        mod.__loader__ = self
        mod.__package__ = fullname.rpartition(".")[0]
        exec(code, mod.__dict__)
        return mod

    def get_code(self, fullname):
        src = self.get_source(fullname)
        return compile(src, self.get_filename(fullname), "exec")

    def get_data(self, path) -> bytes:
        pass

    def get_filename(self, fullname: str):
        return self._baseurl + "/" + fullname.split(".")[-1] + ".py"

    def get_source(self, fullname: str) -> Optional[str]:
        filename = self.get_filename(fullname)
        log.debug("loader: reading %r", filename)
        if filename in self._source_cache:
            log.debug("loader: cached %r", filename)
            return self._source_cache[filename]
        try:
            u = urlopen(filename)
            source = u.read().decode("utf-8")
            log.debug("loader: %r loaded", filename)
            self._source_cache[filename] = source
            return source
        except (HTTPError, URLError) as e:
            log.debug("loader: %r failed. %s", filename, e)
            raise ImportError("cannot load %s" % filename)

    def is_package(self, fullname: str) -> bool:
        return False


class UrlPackageLoader(UrlModuleLoader):
    def load_module(self, fullname: str) -> types.ModuleType:
        mod = super().load_module(fullname)
        mod.__path__ = [self._baseurl]
        mod.__package__ = fullname

    def get_filename(self, fullname: str):
        return self._baseurl + "/" + "__init__.py"

    def is_package(self, fullname: str) -> bool:
        return True


_installed_meta_cache = {}


def install_meta(address):
    if address not in _installed_meta_cache:
        finder = UrlMetaFinder(address)
        _installed_meta_cache[address] = finder
        sys.meta_path.append(finder)
        log.debug("%r installed on sys.meta_path", finder)


def remove_meta(address):
    if address in _installed_meta_cache:
        finder = _installed_meta_cache.pop(address)
        sys.meta_path.remove(finder)
        log.debug("%r removed from sys.meta_path", finder)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    install_meta("http://localhost:15000")
    import fib
    import spam
    import grok.blah

    print(grok.blah.__file__)
    print(grok.__file__)
