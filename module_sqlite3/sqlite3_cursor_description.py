import sqlite3


if __name__ == "__main__":
    db_filename = "todo.db"

    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
        select *
        from task
        where project = 'pymotw'
        """
        )

        print("Task table has these columns:")
        for colinfo in cursor.description:
            print(colinfo)
