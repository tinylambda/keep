from typing import List, Set


class Task:
    depends = None


class A(Task):
    depends = []


class B(Task):
    depends = [A]


class C(Task):
    depends = [B, A]


class D(Task):
    depends = [C, A]


class E(Task):
    depends = [D, B]


class F(Task):
    depends = [B, C]


all_tasks = {F, E, D, C, B, A}


def depends_resolve(ready_tasks: Set[Task], todo_tasks: Set[Task]):
    for todo_task in todo_tasks:
        if not todo_task.depends == 0:
            ready_tasks.add(todo_task)

    new_todo_tasks = todo_tasks - ready_tasks


if __name__ == "__main__":
    depends_resolve(set(), all_tasks)
