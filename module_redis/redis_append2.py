from module_redis import redis_client


KEY = "ts"
redis_client.append(KEY, "0043")
redis_client.append(KEY, "0035")

result = redis_client.getrange(KEY, 0, 3)
print(result)
result = redis_client.getrange(KEY, 4, 7)
print(result)
