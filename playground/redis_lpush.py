import redis
import time


if __name__ == '__main__':
    r = redis.Redis(password='rpassword', db=14)
    q = 'INPUT_2'
    q2 = 'q_role_get_online'
    for i in range(1000):
        d = r.lpush(q, 2 * i)
        print('1', d)
        d = r.lpush(q2, i)
        print('2', d)

    print('...........................')
    time.sleep(6)
    print('1', r.llen(q))
    print('2', r.llen(q2))

