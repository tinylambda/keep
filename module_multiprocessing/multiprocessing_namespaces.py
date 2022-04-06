import multiprocessing


def producer(ns, event):
    ns.value = 'This is the value'
    event.set()


def consumer(ns, event):
    try:
        print('Before event: {}'.format(ns.value))
    except Exception as err:
        print('Before event, error: ', str(err))
    event.wait()
    print('After event:', ns.value)


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    # Any named value added to the Namespace is visible to all of the clients that receive the Namespace instance.
    namespace = mgr.Namespace()
    namespace.value = 'Init value'
    event = multiprocessing.Event()
    p = multiprocessing.Process(target=producer, args=(namespace, event))
    c = multiprocessing.Process(target=consumer, args=(namespace, event))

    c.start()
    p.start()

    c.join()
    p.join()
