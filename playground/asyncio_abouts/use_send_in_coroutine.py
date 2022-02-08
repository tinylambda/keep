from queue import Queue


class Task:
    task_id = 0

    def __init__(self, target):
        self.__class__.task_id += 1
        self.tid = self.__class__.task_id
        self.target = target
        self.sendval = None

    def run(self):
        return self.target.send(self.sendval)


class SystemCall:
    def handle(self):
        pass

    def __await__(self):
        return (yield self)


class Scheduler:
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}

    def new(self, target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def exit(self, task):
        print('Task %d terminated' % task.tid)
        del self.taskmap[task.tid]

    def schedule(self, task):
        self.ready.put(task)

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
                if isinstance(result, SystemCall):
                    result.task = task
                    result.sched = self
                    result.handle()
                    continue
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)


class GetTid(SystemCall):
    def handle(self):
        self.task.sendval = self.task.tid
        self.sched.schedule(self.task)


class YieldControl(SystemCall):
    def handle(self):
        self.task.sendval = None
        self.sched.schedule(self.task)


if __name__ == '__main__':
    # a target
    async def foo():
        mytid = await GetTid()
        for i in range(3):
            print('I am foo', mytid)
            await YieldControl()

    # another target
    async def bar():
        mytid = await GetTid()
        for i in range(5):
            print('I am bar', mytid)
            await YieldControl()

    sched = Scheduler()
    sched.new(foo())
    sched.new(bar())
    sched.mainloop()
