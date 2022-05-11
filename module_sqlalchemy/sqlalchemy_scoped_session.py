import logging
import sys

import sqlalchemy.orm
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    Sequence,
    String,
    ForeignKey,
    select,
)
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


Base = declarative_base()

metadata = MetaData()  # Define tables within it
users = Table(
    'users',
    metadata,
    Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
    Column('name', String(50)),
    Column('fullname', String(50)),
)

addresses = Table(
    'addresses',
    metadata,
    Column('id', Integer, Sequence('addresses_id_seq'), primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String(64), nullable=False),
)

if __name__ == '__main__':
    # With `echo` enabled, we’ll see all the generated SQL produced
    engine = create_engine('sqlite:///:memory:', echo=True)
    # https://stackoverflow.com/questions/6519546/scoped-sessionsessionmaker-or-plain-sessionmaker-in-sqlalchemy
    # scoped session for thread safety
    Session = scoped_session(sessionmaker())
    Session.configure(
        bind=engine, autocommit=False, autoflush=False, expire_on_commit=False
    )

    logging.info('All tables in metadata now:')
    for table_obj in metadata.sorted_tables:
        logging.info('%s', table_obj)

    logging.info('Create all tables')
    metadata.create_all(bind=engine)

    logging.info('Insert some records')
    user_insert = users.insert().values(name='Felix', fullname='Felix Pan')
    logging.info('%s, %s', user_insert, user_insert.compile().params)

    session: sqlalchemy.orm.Session = Session()
    session.execute(user_insert)

    logging.info('Query users by session')
    result = session.query(users)
    logging.info('Result type: [%s]', type(result))
    for item in result:
        logging.info('Got: %s [%s]', item, type(item))

    logging.info('Query users by connection')
    connection = engine.connect()
    result = connection.execute(select(users))
    logging.info('Result type: [%s]', type(result))
    for item in result:
        logging.info('Got: %s [%s]', item, type(item))

    session.execute(users.update().where(users.c.id == 1).values(name='New Name'))

    logging.info('Query by session')
    for item in session.query(users):
        logging.info('Got: %s', item)

    logging.info('Query by connection')
    for item in connection.execute(select(users)):
        logging.info('Got: %s', item)

    logging.info('Rollback!')
    session.rollback()

    logging.info('Query by session')
    for item in session.query(users):
        logging.info('Got: %s', item)

    logging.info('Query by connection')
    for item in connection.execute(select(users)):
        logging.info('Got: %s', item)

    update_sql_x = users.update().where(users.c.id == 1).values(name='Felix')
    update_sql_y = update_sql_x.where(users.c.name == 'felix')
    logging.info('update_sql_x = %s', update_sql_x)
    logging.info('update_sql_y = %s', update_sql_y)
