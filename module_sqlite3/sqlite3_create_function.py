import codecs
import sqlite3


def encrypt(s):
    print('Encrypting {!r}'.format(s))
    return codecs.encode(s, 'rot-13')


def decrypt(s):
    print('Decrypting {!r}'.format(s))
    return codecs.decode(s, 'rot-13')


if __name__ == '__main__':
    db_filename = 'todo.db'

    with sqlite3.connect(db_filename) as conn:
        conn.create_function('encrypt', 1, encrypt)
        conn.create_function('decrypt', 1, decrypt)
        cursor = conn.cursor()

        # Raw values
        print('Original values:')
        query = 'select id, details from task'
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)

        print('\nEncrypting...')
        query = 'update task set details = encrypt(details)'
        cursor.execute(query)

        print('\nRaw encrypted values:')
        query = 'select id, details from task'
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)

        print('\nDecrypting in query...')
        query = 'select id, decrypt(details) from task'
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)

        print('\nDecrypting...')
        query = 'update task set details = decrypt(details)'
        cursor.execute(query)
