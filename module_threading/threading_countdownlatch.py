import threading
import time
import random


class CountDownLatch:
    def __init__(self, count=1):
        self.count = count
        self.condition = threading.Condition()

    def count_down(self):
        with self.condition:
            self.count -= 1
            if self.count < 1:
                self.condition.notifyAll()

    def wait(self):
        with self.condition:
            while (
                self.count > 0
            ):  # always check count to prevent depending tasks wrongly notifyAll
                print("Still wait!")
                self.condition.wait()


def check_task(what, count_down_latch):
    print(f"Checking for {what}...")
    time.sleep(random.randint(0, 5))
    print(f"done for checking {what}")
    count_down_latch.count_down()


def main_task(what, count_down_latch):
    print(f"({what}) waiting for check tasks to complete")
    count_down_latch.wait()
    print(f"({what}) can go on now!")


if __name__ == "__main__":
    cdl = CountDownLatch(3)
    check_redis = threading.Thread(target=check_task, args=("Redis", cdl))
    check_mysql = threading.Thread(target=check_task, args=("MySQL", cdl))
    check_es = threading.Thread(target=check_task, args=("ES", cdl))

    main_task_1 = threading.Thread(target=main_task, args=("Feeding data to ES", cdl))
    main_task_2 = threading.Thread(
        target=main_task, args=("Feeding data to Redis", cdl)
    )

    threads = [main_task_1, main_task_2, check_mysql, check_es, check_redis]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Done")
