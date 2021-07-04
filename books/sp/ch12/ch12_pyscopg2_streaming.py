"""
--- create database
CREATE TABLE message (
     id SERIAL PRIMARY KEY,
     channel INTEGER NOT NULL,
     source TEXT NOT NULL,
     content TEXT NOT NULL
);
--- create function
CREATE OR REPLACE FUNCTION notify_on_insert() RETURNS trigger AS $$ BEGIN
     PERFORM pg_notify('channel_' || NEW.channel,
                       CAST(row_to_json(NEW) AS TEXT));
     RETURN NULL;
   END;
   $$ LANGUAGE plpgsql;
--- create trigger
CREATE TRIGGER notify_on_message_insert AFTER INSERT ON message
   FOR EACH ROW EXECUTE PROCEDURE notify_on_insert();
"""
import psycopg2
import psycopg2.extensions
import select


if __name__ == '__main__':
    conn = psycopg2.connect(database='mydatabase', user='postgres', password='postgrespass', host='localhost')
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    curs = conn.cursor()
    curs.execute('LISTEN channel_1;')

    while True:
        select.select([conn], [], [])
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop()
            print('Got NOTIFY:', notify.pid, notify.channel, notify.payload)

