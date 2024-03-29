from concurrent import futures

from books.fp.ch17.ch17_1 import save_flag, get_flag, show, main


MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ProcessPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))


if __name__ == "__main__":
    main(download_many)
