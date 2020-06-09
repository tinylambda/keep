from module_redis import redis_client


size = redis_client.dbsize()
print(size)

