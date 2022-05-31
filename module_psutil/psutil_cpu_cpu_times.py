import logging
import pprint
import sys

import psutil

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


if __name__ == "__main__":
    logging.info("Default: ")
    pprint.pprint(psutil.cpu_times())

    logging.info("percpu = True: ")
    pprint.pprint(psutil.cpu_times(percpu=True))

    # user: time spent by normal processes executing in user mode; on Linux this also includes guest time

    # system: time spent by processes executing in kernel mode

    # idle: time spent doing nothing

    # nice (UNIX): time spent by niced (prioritized) processes executing in user mode;
    # on Linux this also includes guest_nice time

    # iowait (Linux): time spent waiting for I/O to complete. This is not accounted in idle time counter.

    # irq (Linux, BSD): time spent for servicing hardware interrupts

    # softirq (Linux): time spent for servicing software interrupts

    # steal (Linux 2.6.11+): time spent by other operating systems running in a virtualized environment

    # guest (Linux 2.6.24+): time spent running a virtual CPU for guest operating systems
    # under the control of the Linux kernel

    # guest_nice (Linux 3.2.0+): time spent running a niced guest
    # (virtual CPU for guest operating systems under the control of the Linux kernel)
