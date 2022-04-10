import sqlite3


def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name, description from project')
    for name, desc in cursor.fetchall():
        print(' ', name)


if __name__ == '__main__':
    db_filename = 'todo.db'
    with sqlite3.connect(db_filename) as conn:
        try:
            cursor = conn.cursor()
            cursor.execute('delete from project where name="virtualenvwrapper"')

            print('\nAfter delete:')
            show_projects(conn)

            raise RuntimeError('simulated error')
        except Exception as err:
            print('ERROR:', err)
            conn.rollback()
        else:
            conn.commit()

        print('\nAfter rollback:')
        show_projects(conn)
