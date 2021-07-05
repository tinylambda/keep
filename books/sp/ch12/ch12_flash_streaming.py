import flask
import psycopg2
import psycopg2.extensions
import select


app = flask.Flask(__name__)


def stream_messages(channel):
    conn = psycopg2.connect(database='mydatabase', user='postgres', password='postgrespass', host='localhost')
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    curs = conn.cursor()
    curs.execute('LISTEN channel_1;')

    while True:
        select.select([conn], [], [])
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop()
            yield f'data: {notify.payload}\n\n'


@app.route('/message/<channel>', methods=['GET'])
def get_messages(channel):
    """use SSE to push events to client"""
    return flask.Response(stream_messages(channel))


if __name__ == '__main__':
    app.run()

