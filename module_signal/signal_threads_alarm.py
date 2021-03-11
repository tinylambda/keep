import signal
import time
import threading


# Although alarms can be set in any thread, they are always received by the main thread.
def signal_handler(num, stack):
    print(time.ctime(), 'Alarm in', threading.current_thread().name)


signal.signal(signal.SIGALRM, signal_handler)


def use_alarm():
    t_name = threading.current_thread().name
    print(time.ctime(), 'Setting alarm in', t_name)
    signal.alarm(1)
    print(time.ctime(), 'Sleeping in', t_name)
    time.sleep(3)
    print(time.ctime(), 'Done with sleep in', t_name)


alarm_thread = threading.Thread(target=use_alarm, name='alarm_thread')
alarm_thread.start()
time.sleep(0.1)

print(time.ctime(), 'Waiting for', alarm_thread.name)
alarm_thread.join()

print(time.ctime(), 'Exiting normally')

