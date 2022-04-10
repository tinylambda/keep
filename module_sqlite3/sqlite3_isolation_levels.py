import logging
import sqlite3
import sys
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-10s) %(message)s',
)


def writer(db_name, isolation_level_name, ready_event):
    with sqlite3.connect(db_name, isolation_level=isolation_level_name) as conn:
        cursor = conn.cursor()
        cursor.execute('update task set priority = priority + 1')
        logging.debug('waiting to synchronize')
        ready_event.wait()
        logging.debug('PAUSING')
        time.sleep(1)
        conn.commit()
        logging.debug('CHANGES COMMITTED')


def reader(db_name, isolation_level_name, ready_event):
    with sqlite3.connect(db_name, isolation_level=isolation_level_name) as conn:
        cursor = conn.cursor()
        logging.debug('waiting to synchronize')
        ready_event.wait()
        logging.debug('wait over')
        cursor.execute('select * from task')
        logging.debug('SELECT EXECUTED')
        cursor.fetchall()
        logging.debug('results fetched')


if __name__ == '__main__':
    db_filename = 'todo.db'
    isolation_level = sys.argv[1]
    ready = threading.Event()

    threads = [
        threading.Thread(name='Reader 1', target=reader, args=(db_filename, isolation_level, ready)),
        threading.Thread(name='Reader 2', target=reader, args=(db_filename, isolation_level, ready)),
        threading.Thread(name='Writer 1', target=writer, args=(db_filename, isolation_level, ready)),
        threading.Thread(name='Writer 2', target=writer, args=(db_filename, isolation_level, ready)),
    ]

    [t.start() for t in threads]

    time.sleep(1)
    logging.debug('setting ready')
    ready.set()

    [t.join() for t in threads]


"""
python sqlite3_isolation_levels.py DEFERRED
python sqlite3_isolation_levels.py IMMEDIATE
python sqlite3_isolation_levels.py EXCLUSIVE
"""
