import time

import redis

if __name__ == "__main__":
    redis_client = redis.Redis(password="rpassword", db=14)
    q_name = "q_role_get_input"
    for i in range(1000):
        redis_client.lpush(q_name, f"role_online:{i}")
        redis_client.lpush(q_name, f"role_input:a=1&b=2&c=3&role_id={i}")

    l = redis_client.llen(q_name)

    start = time.time()
    while l > 0:
        print("processing")
        time.sleep(0.001)
        l = redis_client.llen(q_name)
    print(f"cost: {time.time() - start} seconds")
