from threading import Semaphore
import urllib.request


_fetch_url_sema = Semaphore(5)


def fetch_url(url):
    with _fetch_url_sema:
        return urllib.request.urlopen(url)


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor

    executor = ThreadPoolExecutor(max_workers=8)
    request_url = "http://www.baidu.com"

    futs = []
    for _ in range(10):
        fut = executor.submit(fetch_url, request_url)
        futs.append(fut)
    executor.shutdown(wait=True)

    for fut in futs:
        print(fut.result().read()[:10])
