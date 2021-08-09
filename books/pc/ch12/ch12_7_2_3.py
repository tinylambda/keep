from concurrent.futures import ThreadPoolExecutor
import urllib.request
import ssl

context = ssl._create_unverified_context()


def fetch_url(url):
    u = urllib.request.urlopen(url, context=context)
    data = u.read()
    return data


if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)
    a = pool.submit(fetch_url, 'http://www.python.org')
    b = pool.submit(fetch_url, 'http://www.pypy.org')

    x = a.result()
    y = b.result()

    print(x)
    print(y)
