from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence
from sqlalchemy.sql import select, and_, or_, not_, text


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
stmt = text("SELECT * FROM users WHERE users.name BETWEEN :x AND :y")
stmt = stmt.bindparams(x="m", y="z")
for item in connection.execute(stmt):
    print(item)


