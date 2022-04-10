import sqlite3
import sys


if __name__ == '__main__':
    db_filename = 'todo.db'
    sql = 'select id, details, deadline from task'

    def show_deadline(conn):
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        for col in ['id', 'details', 'deadline']:
            print('{:<8} {!r:<26} {}'.format(col, row[col], type(row[col])))

    print('Without type detection:')
    with sqlite3.connect(db_filename) as conn:
        show_deadline(conn)

    #  Use PARSE_DECLTYPES if the column was declared using the desired type when the table was defined.
    print('\nWith type detection:')
    with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
        show_deadline(conn)
