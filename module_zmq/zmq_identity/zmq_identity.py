import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def s_dump(s: zmq.Socket):
    logging.info("%s", "-" * 32)
    while True:
        msg = s.recv()
        logging.info("Received: [%s]", msg)
        more = s.getsockopt(zmq.RCVMORE)
        if more == 0:
            break


if __name__ == "__main__":
    context = zmq.Context()

    sink = context.socket(zmq.ROUTER)
    sink.bind("inproc://example")

    anonymous = context.socket(zmq.REQ)
    anonymous.connect("inproc://example")
    anonymous.send(b"ROUTER uses a generated UUID")
    s_dump(sink)

    identified = context.socket(zmq.REQ)
    identified.setsockopt(zmq.IDENTITY, b"PEER2")
    identified.connect("inproc://example")
    identified.send(b"ROUTER socket uses REQ's socket identity")
    s_dump(sink)

    sink.send(b"PEER2", zmq.SNDMORE)
    sink.send(b"", zmq.SNDMORE)
    sink.send(b"good")
    s_dump(identified)

    identified.send(
        b"hello"
    )  # if commented out zmq.error.ZMQError: Operation cannot be accomplished in current state
    sink.send(b"PEER2", zmq.SNDMORE)
    sink.send(b"", zmq.SNDMORE)
    sink.send(b"hello again")
    s_dump(identified)
    # poller = zmq.Poller()
    # poller.register(sink, zmq.POLLIN)
    # while True:
    #     socks = poller.poll()
    #     for sock, mask in socks:
    #         id_ = sock.recv()
    #         blank_ = sock.recv()
    #         content_ = sock.recv()
    #         logging.info('\n%s\n%s\n%s\n', id_, blank_, content_)
