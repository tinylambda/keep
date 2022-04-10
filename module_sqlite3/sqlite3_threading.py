import sqlite3
import sys
import threading
import time


def reader(conn):
    print('Starting thread')
    try:
        cursor = conn.cursor()
        cursor.execute('select * from task')
        cursor.fetchall()
        print('results fetched')
    except Exception as err:
        print('ERROR:', err)


if __name__ == '__main__':
    db_filename = 'todo.db'
    isolation_level = None  # auto commit

    with sqlite3.connect(db_filename, isolation_level=isolation_level) as conn:
        t = threading.Thread(name='Reader 1', target=reader, args=(conn, ))
        t.start()
        t.join()
