import collections
import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class Connection:
    socket = attr.ib()

    @classmethod
    def connect(cls, db_string):
        return cls(socket=42)


@attr.s
class ConnectionPool:
    db_string = attr.ib()
    pool = attr.ib(default=attr.Factory(collections.deque))
    debug = attr.ib(default=False)

    def get_connection(self):
        try:
            return self.pool.pop()
        except IndexError:
            if self.debug:
                logging.debug('new connection!')
            return Connection.connect(self.db_string)

    def free_connection(self, conn):
        if self.debug:
            logging.debug('connection returned!')
        self.pool.appendleft(conn)


if __name__ == '__main__':
    cp = ConnectionPool('postgres://localhost')
    logging.info('%s', cp)

    conn = cp.get_connection()
    logging.info('%s', conn)
    cp.free_connection(conn)
    logging.info('%s', cp)
