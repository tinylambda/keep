class CacheBackend:
    @staticmethod
    def get(cache, key):
        raise NotImplementedError()

    @staticmethod
    def set(cache, key, value):
        raise NotImplementedError()

    @staticmethod
    def delete(cache, key):
        raise NotImplementedError()


class LocalCacheBackend(CacheBackend):
    @staticmethod
    def get(cache, key):
        pass

    @staticmethod
    def set(cache, key, value):
        pass

    @staticmethod
    def delete(cache, key):
        pass


class SimpleCache:
    def __init__(self, backend: CacheBackend):
        self._backend = backend

    def get(self, key):
        return self._backend.get(self, key)

    def set(self, key, value):
        return self._backend.set(self, key, value)

    def delete(self, key):
        return self._backend.delete(self, key)


if __name__ == '__main__':
    sc = SimpleCache(LocalCacheBackend())
    sc.get("x")



