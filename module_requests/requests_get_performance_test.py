import time
import requests


URL1 = 'http://127.0.0.1:10000'
URL2 = 'http://localhost:8000/chat/cc/'


if __name__ == '__main__':
    start = time.time()
    ex_count = 0

    for i in range(10000):
        try:
            response = requests.get(URL2)
            if response.status_code != 200:
                print(response.status_code)
        except Exception as e:
            ex_count += 1
            print(e)
            print('-' * 64)

    print('Cost: ', time.time() - start)
    print('Exception count: ', ex_count)

