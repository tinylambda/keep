import multiprocessing
import random
import zmq


def compute():
    return sum([random.randint(1, 100) for _ in range(1000000)])


def worker():
    context_inside = zmq.Context()
    worker_receiver = context_inside.socket(zmq.PULL)
    worker_receiver.connect('tcp://0.0.0.0:5555')
    result_sender = context_inside.socket(zmq.PUSH)
    result_sender.connect('tcp://0.0.0.0:5556')
    poller = zmq.Poller()
    poller.register(worker_receiver, zmq.POLLIN)

    while True:
        socks = dict(poller.poll())
        if socks.get(worker_receiver) == zmq.POLLIN:
            obj = worker_receiver.recv_pyobj()
            result_sender.send_pyobj(obj())


if __name__ == '__main__':
    context = zmq.Context()
    # build a channel to send work to be done
    work_sender = context.socket(zmq.PUSH)
    work_sender.bind('tcp://0.0.0.0:5555')
    # build a channel to receive computed results
    result_receiver = context.socket(zmq.PULL)
    result_receiver.bind('tcp://0.0.0.0:5556')
    # start 8 workers
    processes = []
    for _ in range(8):
        p = multiprocessing.Process(target=worker)
        p.start()
        processes.append(p)

    # send 8 jobs
    for _ in range(8):
        work_sender.send_pyobj(compute)

    # read 8 results
    results = []
    for x in range(8):
        results.append(result_receiver.recv_pyobj())

    # terminate all processes
    for p in processes:
        p.terminate()
    print('results: %s', results)

