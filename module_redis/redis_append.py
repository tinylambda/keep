from module_redis import redis_client


KEY = "append_example_key"

key_exists = redis_client.exists(KEY)
print(f"{KEY} exists? :", key_exists)

append_result = redis_client.append(KEY, "Hello")
print(append_result)
append_result = redis_client.append(KEY, " World")
print(append_result)

final_value = redis_client.get(KEY)
print(final_value)
