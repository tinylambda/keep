import multiprocessing


def producer(ns, event):
    ll = ns.my_list
    ll.append("This is the value")
    # To update the list, attach it to the namespace object again.
    # ns.my_list = ll
    event.set()


def consumer(ns, event):
    print("Before event:", ns.my_list)
    event.wait()
    print("After event:", ns.my_list)


if __name__ == "__main__":
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    namespace.my_list = ["a"]

    event = multiprocessing.Event()
    p = multiprocessing.Process(target=producer, args=(namespace, event))
    c = multiprocessing.Process(target=consumer, args=(namespace, event))

    c.start()
    p.start()

    c.join()
    p.join()
