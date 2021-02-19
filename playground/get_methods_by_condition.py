class A:
    def __init__(self):
        self._tasks = []

    @property
    def tasks(self):
        if not self._tasks:
            for item in dir(self):
                if item.startswith('task_'):
                    item_value = getattr(self, item)
                    if callable(item_value):
                        self._tasks.append(item_value)
        return self._tasks

    def task_a(self):
        pass

    def task_b(self):
        pass

    def task_c(self):
        pass

    def f(self):
        pass


if __name__ == '__main__':
    a = A()
    print(a.tasks)
    for item in a.tasks:
        print(item())


