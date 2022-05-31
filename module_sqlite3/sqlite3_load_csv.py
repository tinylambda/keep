import csv
import sqlite3
import sys


if __name__ == "__main__":
    db_filename = "todo.db"
    data_filename = sys.argv[1]

    sql = """
    insert into task (details, priority, status, deadline, project)
    values (:details, :priority, 'active', :deadline, :project)
    """

    with open(data_filename, "rt") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            cursor.executemany(sql, csv_reader)
