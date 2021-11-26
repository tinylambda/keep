# https://docs.sqlalchemy.org/en/13/core/tutorial.html
import logging

import sqlalchemy.orm
from sqlalchemy import create_engine, update, delete
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence
from sqlalchemy.sql import select, and_, or_, not_, text, table, literal_column, func, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


metadata = MetaData()  # Define tables within it
users = Table(
    'users', metadata,
    Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
    Column('name', String(50)),
    Column('fullname', String(50)),
)

addresses = Table(
    'addresses', metadata,
    Column('id', Integer, Sequence('addresses_id_seq'), primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String(64), nullable=False),
)

print('All tables in metadata now:')
for table_obj in metadata.sorted_tables:
    print(table_obj)

print('Now create a engine to create theses tables in a database: ')
# With `echo` enabled, we’ll see all the generated SQL produced
engine = create_engine('sqlite:///:memory:', echo=True)

print(f'Create tables in engine {engine}')
metadata.create_all(bind=engine)

print('Create a insert object: ')
user_insert = users.insert()
print(user_insert)

print('Create a insert with limited values: ')
user_insert = users.insert().values(name='felix', fullname='Felix Pan')
print(user_insert)

print('Insert object\'s params: ')
print(user_insert.compile().params)

print('Get a connection from engine: ')
connection = engine.connect()
print(connection)

print('Now, use this connection to execute our insert object: ')
result = connection.execute(user_insert)
print(f'The inserted row\'s primary key is: {result.inserted_primary_key}')

print('Create a generic Insert statement again and use it in the "normal" way: ')
user_insert = users.insert()
connection.execute(user_insert, id=2, name='wendy', fullname='Wendy Williams')
connection.execute(user_insert, name='jane', fullname='Jane Bush')

address_insert = addresses.insert()
print('Insert multiple addresses in one run: ')
connection.execute(address_insert, [
    {'user_id': 1, 'email_address': 'felix@yahoo.com'},
    {'user_id': 1, 'email_address': 'felix@gmail.com'},
    {'user_id': 2, 'email_address': 'wendy@qq.com'},
    {'user_id': 3, 'email_address': 'jane@163.com'},
    {'user_id': 3, 'email_address': 'jane@126.com'},
])

print('\nNow we have some data ready, select users: ')
s = select([users])
result = connection.execute(s)
for item in result:
    print(item)

print('\nIf iterate over the result again, print nothing (cursor like): ')
for item in result:
    print(item)

print('\nExecute the select statement again to fetch one row: ')
result = connection.execute(s)
row = result.fetchone()
print('name: ', row['name'], '; fullname: ', row['fullname'])

print('\nUse index to retrieve column data: ')
row = result.fetchone()
print('name: ', row[1], '; fullname: ', row[2])

print('\nUse Column objects to retrieve column data: ')
row = result.fetchone()
print('name: ', row[users.c.name], '; fullname: ', row[users.c.fullname])

print('\nClose the cursor (result) explicitly: ')
result.close()

print('\nSelect specific columns: ')
s = select([users.c.name, users.c.fullname])  # No id column here
result = connection.execute(s)
for row in result:
    print(row)

print('\nWhat about a select relating to two tables (Cartesian product produced!): ')
s = select([users, addresses])
for row in connection.execute(s):
    print(row)

print('\nUse where clause to avoid Cartesian product: ')
s = select([users, addresses]).where(users.c.id == addresses.c.user_id)
for row in connection.execute(s):
    print(row)

print('\nOperators explore: ')
print('users.c.id == addresses.c.user_id =>', users.c.id == addresses.c.user_id)
print('users.c.id == 7 =>', users.c.id == 7)
print('users.c.id == 7 params =>', (users.c.id == 7).compile().params)
print('users.c.id != 7 =>', users.c.id != 7)
print('users.c.name == None =>', users.c.name == None)
print('"fred" > users.c.name =>', "fred" > users.c.name)
print('users.c.id + addresses.c.id =>', users.c.id + addresses.c.id)
print('users.c.name + users.c.fullname =>', (users.c.name + users.c.fullname).compile(bind=engine))
print('If use mysql =>', (users.c.name + users.c.fullname).compile(bind=create_engine('mysql+mysqlconnector://')))

print('\nConjunctions: ')
print(
    and_(
        users.c.name.like('j%'),
        users.c.id == addresses.c.user_id,
        or_(
            addresses.c.email_address == 'jane@126.com',
            addresses.c.email_address == 'jane@qq.com'
        ),
        not_(users.c.id > 15)
    )
)

print('\nNow a full select statement: ')
s = select([
    (users.c.fullname + ', ' + addresses.c.email_address).label('title')
]).where(
    and_(
        users.c.id == addresses.c.user_id,
        users.c.name.between('m', 'z'),
        or_(
            addresses.c.email_address.like('%@aol.com'),
            addresses.c.email_address.like('%@qq.com')
        )
    )
)
for item in connection.execute(s):
    print(item)

print('\nAnother form: ')
s = select([
    (users.c.fullname + ', ' + addresses.c.email_address).label('title')
]).where(
    users.c.id == addresses.c.user_id
).where(
    users.c.name.between('m', 'z')
).where(
    or_(
        addresses.c.email_address.like('%@aol.com'),
        addresses.c.email_address.like('%@qq.com')
    )
)
for item in connection.execute(s):
    print(item)

print('\nUse raw SQL by using text(): ')
s = text(
    "SELECT users.fullname || ', ' || addresses.email_address AS title "
        "FROM users, addresses "
        "WHERE users.id = addresses.user_id "
        "AND users.name BETWEEN :x AND :y "
        "AND (addresses.email_address LIKE :e1 "
              "OR addresses.email_address LIKE :e2)"
)
for item in connection.execute(
    s, x='m', y='z', e1='%@aol.com', e2='%@qq.com'
):
    print(item)

print('\nPre-established bound values: ')
s = text("SELECT * FROM users WHERE users.name BETWEEN :x AND :y")
s = s.bindparams(x="m", y="z")
for item in connection.execute(s):
    print(item)


print('\nSpecify information about the result columns: ')
s = text('SELECT id, name FROM users')
s = s.columns(id=Integer, name=String)
for item in connection.execute(s):
    print(item)

# s = text('SELECT id, name FROM users')
# s = s.columns(users.c.id, users.c.name)
# j = s.join(addresses, s.c.id == addresses.c.user_id)
# new_s = select([s.c.id, addresses.c.id]).select_from(j).where(s.c.name == 'x')
# for item in connection.execute(new_s):
#     print(item)
s = text(
    'SELECT users.id, addresses.id, users.id, '
    'users.name, addresses.email_address AS email '
    'FROM users JOIN addresses ON users.id=addresses.user_id '
    'WHERE users.id = 1'
).columns(
    users.c.id,
    addresses.c.id,
    addresses.c.user_id,
    users.c.name,
    addresses.c.email_address
)
for item in connection.execute(s):
    print(item)

print('\nUse more specific text with table(), literal_column() and column(): ')
s = select([
    literal_column('users.fullname', String) +
    ', ' +
    literal_column('addresses.email_address').label('title')
]).where(
    and_(
        literal_column('users.id') == literal_column('addresses.user_id'),
        text('users.name BETWEEN "m" and "z"'),
        text(
            '(addresses.email_address LIKE :x OR '
            'addresses.email_address LIKE :y)'
        )
    )
).select_from(table('users')).select_from(table('addresses'))

for item in connection.execute(s, x='%@qq.com', y='%@aol.com'):
    print(item)

print('\nOrdering or Grouping by Label: ')
s = select([
    addresses.c.user_id,
    func.count(addresses.c.id).label('num_addresses')
]).group_by('user_id').order_by(desc('user_id'), 'num_addresses',)
for item in connection.execute(s):
    print(item)

print('\nUsing aliases and subqueries: ')
a1 = addresses.alias('a1')
a2 = addresses.alias('a2')
s = select([users]).where(
    and_(
        users.c.id == a1.c.user_id,
        users.c.id == a2.c.user_id,
        a1.c.email_address == 'felix@yahoo.com',
        a2.c.email_address == 'felix@gmail.com'
    )
)
for item in connection.execute(s):
    print(item)


print('\nUsing Joins: ')
print(users.join(addresses))  # automatically detect the ON clause based on the ForeignKey
print(
    users.join(addresses, addresses.c.email_address.like(users.c.name + '%'))
)

s = select([users.c.fullname]).select_from(
    users.join(addresses, addresses.c.email_address.like(users.c.name + '%'))
)
for item in connection.execute(s):
    print(item)

print('\nTable CTE:')
users_cte = select([users.c.id, users.c.name]).where(users.c.name == 'felix').cte(name="my_name")
s = select([addresses]).where(addresses.c.user_id == users_cte.c.id)
for item in connection.execute(s):
    print(item)


print('\n\nPlay with session: ')
# Create a configured Session class
Session = sessionmaker(bind=engine, autoflush=False)

# Create a Session object
session: sqlalchemy.orm.Session = Session(autocommit=False)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return f'<User(name="{self.name}", fullname="{self.fullname}")>'


demo_user_1 = User(name='demo1', fullname='Demo1')
demo_user_2 = User(name='demo2', fullname='Demo2')

print('Add to session but do not commit[demo1, demo2]')
session.add(demo_user_1)
session.add(demo_user_2)

print('Session.execute but not commit [demo3]')
session.execute(users.insert(), [
    {'name': 'demo3', 'fullname': 'Demo3'},
])

print('Query before commit')
for item in session.query(User):
    print(item)
# session.rollback()  # this will dismiss demo3

print('Select before commit [demo3 exists]')
for item in connection.execute(select([users])):
    print(item)

session.commit()

print('Query after commit')
for item in session.query(User):
    print(item)

print('Select after commit')
for item in connection.execute(select([users])):
    print(item)

update_sql = update(User).where(User.id == 1).values(name='Felix')
print(update_sql)
print(update_sql.compile().params)
print('Update!')
session.execute(update_sql)

print('Query after update')
for item in session.query(User):
    print(item)

print('Delete demo2')
delete_sql = delete(User).where(User.name == 'demo2')
print(delete_sql)
print(delete_sql.compile().params)
print('Delete!')
session.execute(delete_sql)

print('Query after delete')
for item in session.query(User):
    print(item)

print('Rollback...')
session.rollback()
print('Query after rollback')
# found that demo2 came back, if you want delete take effect, use session.commit() or session autocommit = True
for item in session.query(User):
    print(item)

print('Delete use table object')
delete_sql = users.delete().where(users.c.name == 'demo2')
print(delete_sql)
print(delete_sql.compile().params)
print('Delete!')
session.execute(delete_sql)
session.commit()

print('Query after delete')
for item in session.query(User):
    print(item)

print('Use where OR')
for item in session.query(User).where(or_(User.name == "felix", User.name == "jane")):
    print(item)

print('Use where IN')
for item in session.query(User).where(User.name.in_(['felix', 'jane'])):
    print(item)
