import concurrent.futures
import logging
import os
import random
import signal
import sys
import threading
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()
    socket = context.socket(zmq.ROUTER)
    # socket.setsockopt(zmq.RCVHWM, 5)
    # socket.setsockopt(zmq.SNDHWM, 5)
    socket.bind('tcp://*:7777')

    interrupted = False

    def callback(signum, stack):
        global interrupted
        interrupted = True

    signal.signal(signal.SIGINT, callback)
    signal.signal(signal.SIGTERM, callback)

    logging.info('PID is %s', os.getpid())

    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN)
    POLL_TIMEOUT = 3000

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    recv_lock = threading.Lock()
    send_lock = threading.Lock()

    def worker(s):
        thread_name = threading.current_thread().name
        logging.info('waiting for socket (%s) msg in thread %s', s, thread_name)

        def do(msg, addr):
            logging.info('got msg: %s', msg)
            time.sleep(random.random())
            message = f'{thread_name} : '.encode() + msg
            with send_lock:
                s.send(addr, zmq.SNDMORE)
                s.send(message)

        while True:
            with recv_lock:
                addr = s.recv()
                msg = s.recv()
                threading.Thread(target=do, args=(msg, addr), daemon=True).start()
                if interrupted:
                    break

    executor.map(worker, [socket, socket, socket, socket])
