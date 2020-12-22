import json

from module_redis import redis_client


class SimulateSimple:
    def __init__(self, r):
        self.redis_client = r

    def __getitem__(self, item):
        r = self.redis_client.get(item)
        r = json.loads(r)
        return r

    def __setitem__(self, key, value):
        value = json.dumps(value)
        return self.redis_client.set(key, value)


if __name__ == '__main__':
    s = SimulateSimple(redis_client)
    print(s['x'])
    s['x'] = {}
    print(s['x'])


