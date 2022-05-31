import pickle
import sqlite3


def adapter_func(obj):
    print("adapter_func({})".format(obj))
    return pickle.dumps(obj)


def converter_func(data):
    print("converter_func({!r})".format(data))
    return pickle.loads(data)


class MyObj:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return "MyObj({!r})".format(self.arg)


if __name__ == "__main__":
    db_filename = "todo.db"
    sqlite3.register_adapter(MyObj, adapter_func)
    sqlite3.register_converter("MyObj", converter_func)

    to_save = [
        (MyObj("this is a value to save"),),
        (MyObj(42),),
    ]

    with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
        conn.execute(
            """
        drop table if exists obj
        """
        )
        conn.execute(
            """
        create table if not exists obj (
            id integer primary key autoincrement not null,
            data MyObj
            )
        """
        )
        cursor = conn.cursor()

        cursor.executemany("insert into obj (data) values (?)", to_save)
        cursor.execute("select id, data from obj")
        for obj_id, obj in cursor.fetchall():
            print("Retrieved", obj_id, obj)
            print("with type", type(obj))
            print()
