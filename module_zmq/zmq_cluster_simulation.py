import random
import sys
import threading
import time

import zmq


NBR_CLIENTS = 10
NBR_WORKERS = 5


def asbytes(obj):
    s = str(obj)
    if str is not bytes:
        s = s.encode('ascii')
    return s


def client_task(name, i):
    ctx = zmq.Context()
    client = ctx.socket(zmq.REQ)
    client.identity = (u'Client-%s-%s' % (name, i)).encode('ascii')
