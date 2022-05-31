import signal
import threading
import os
import time


def signal_handler(num, stack):
    print("Received signal {} in {}".format(num, threading.current_thread().name))


signal.signal(signal.SIGUSR1, signal_handler)


def wait_for_signal():
    print("Waiting for signal in", threading.current_thread().name)
    signal.pause()
    print("Done waiting")


receiver = threading.Thread(target=wait_for_signal, name="receiver")
receiver.start()
time.sleep(0.1)


def send_signal():
    print("Sending signal in", threading.current_thread().name)
    os.kill(os.getpid(), signal.SIGUSR1)


sender = threading.Thread(target=send_signal, name="sender")
sender.start()
sender.join()

print("Waiting for", receiver.name)
# The signal.alarm(2) call near the end of the example prevents an infinite block,
# since the receiver thread will never exit.
print("before alarm signal")  # printed
signal.alarm(2)
print("after alarm signal")  # printed
receiver.join()
print("after join")  # now printed
