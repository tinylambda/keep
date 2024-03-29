import sqlite3
import sys


if __name__ == "__main__":
    db_filename = "todo.db"
    project_name = sys.argv[1]

    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()

        query = """
        select id, priority, details, status, deadline
        from task
        where project = :project_name
        """

        cursor.execute(query, {"project_name": project_name})
        for row in cursor.fetchall():
            task_id, priority, details, status, deadline = row
            print(
                "{:2d} [{:d}] {:<25} [{:<8}] ({})".format(
                    task_id, priority, details, status, deadline
                )
            )
