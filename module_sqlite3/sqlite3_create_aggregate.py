import sqlite3
import collections


class Mode:
    def __init__(self):
        self.counter = collections.Counter()

    def step(self, value):
        print("step({!r})".format(value))
        self.counter[value] += 1

    def finalize(self):
        result, count = self.counter.most_common(1)[0]
        print("finalize() -> {!r} ({} times)".format(result, count))
        return result


if __name__ == "__main__":
    db_filename = "todo.db"

    with sqlite3.connect(db_filename) as conn:
        conn.create_aggregate("mode", 1, Mode)

        cursor = conn.cursor()
        cursor.execute(
            """
        select mode(deadline)
        from task
        where project = 'pymotw'
        """
        )
        row = cursor.fetchone()
        print("mode(deadline) is:", row[0])
