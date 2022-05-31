import time

from module_redis import redis_client


print("feed normal data")
for i in range(1000):
    key = f"key_{i}"
    value = time.time()
    redis_client.set(key, value)


print("feed zset data")
for i in range(1000):
    key = f"zkey_{i}"
    value = time.time()
    redis_client.zadd("zkey", {key: value})


redis_client.close()
