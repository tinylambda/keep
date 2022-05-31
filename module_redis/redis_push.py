from module_redis import redis_client


value = redis_client.lpush("lkey", "hello")
print(value)
value = redis_client.lpush(b"lkey", b"world")
print(value)
value = redis_client.rpush("lkey", "!")
print(value)
