from module_redis import redis_client


value = redis_client.lpop('lkey')
print(value)

value = redis_client.rpop('lkey')
print(value)

