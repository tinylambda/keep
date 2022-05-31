import time
import requests
import concurrent.futures

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


URL1 = "http://127.0.0.1:10000"
URL2 = "http://localhost:8000/chat/cc/"


def worker(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(response.status_code)
    except Exception as e:
        print(e)
        print("-" * 64)


if __name__ == "__main__":
    start = time.time()

    pool = ThreadPoolExecutor(max_workers=16)
    results = list(pool.map(worker, [URL2 for _ in range(10000)]))
    print(len(results))
    print(results[:10])

    print("Cost: ", time.time() - start)
