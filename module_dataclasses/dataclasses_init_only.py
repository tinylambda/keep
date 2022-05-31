from dataclasses import dataclass
from dataclasses import field
from dataclasses import InitVar


class DatabaseType:
    def lookup(self, name):
        return 100


@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database: DatabaseType):
        if self.j is None and database is not None:
            self.j = database.lookup("j")


if __name__ == "__main__":
    c = C(10, database=DatabaseType())
    print(c)
