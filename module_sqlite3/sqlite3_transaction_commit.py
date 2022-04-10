import sqlite3


def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name, description from project')
    for name, desc in cursor.fetchall():
        print(' ', name)


if __name__ == '__main__':
    db_filename = 'todo.db'
    with sqlite3.connect(db_filename) as conn1:

        cursor1 = conn1.cursor()
        cursor1.execute('delete from project where name="virtualenvwrapper"')
        conn1.commit()

        print('Before changes:')
        show_projects(conn1)

        # insert in one cursor
        cursor1.execute('''
        insert into project (name, description, deadline)
        values ('virtualenvwrapper', 'Virtualenv Extensions', '2022-12-12')
        ''')
        print('After changes in conn1:')
        show_projects(conn1)

        print('\nBefore commit:')
        with sqlite3.connect(db_filename) as conn2:
            show_projects(conn2)

        conn1.commit()  # visible to other clients

        print('\nAfter commit:')
        with sqlite3.connect(db_filename) as conn3:
            show_projects(conn3)
