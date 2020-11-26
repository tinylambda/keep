import time
import requests


if __name__ == '__main__':
    start = time.time()
    for i in range(10000):
        response = requests.get('http://127.0.0.1:8000/')
        if response.status_code != 200:
            print(response.status_code)

    print('Cost: ', time.time() - start)

