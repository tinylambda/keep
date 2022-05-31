import os.path
import papa
import sys
from pprint import pprint

from papa import Papa

if __name__ == "__main__":
    with Papa() as p:
        simple_routine = p.make_process(
            "SimpleRoutine",
            sys.executable,
            args=("simple_routine.py",),
            working_dir=os.path.dirname(__file__),
            stderr=papa.STDOUT,  # pass papa.STDOUT to stderr to merge the streams.
            # bufsize=0,  # If you pass bufsize=0, not output will be recorded.
        )

        watcher = p.watch_processes("SimpleRoutine")
        while True:
            if watcher and watcher.ready:
                out, err, closed = watcher.read()
                pprint([out, err, closed])
                print(b"".join([item.data for item in out]), "!!!")
                if closed:
                    pprint("App closed!")
                    break
        # watcher.acknowledge()
        watcher.close()  # will call acknowledge()
