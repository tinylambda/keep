import os
import signal
import subprocess
import tempfile
import time
import sys


def show_setting_pgrp():
    print('Calling os.setpgrp() from {}'.format(os.getpid()))
    os.setpgrp()
    print('Process group is now {}'.format(os.getpgrp()))
    sys.stdout.flush()


script = '''#!/bin/sh
echo "Shell script in process $$"
set -x
python3 signal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(
    ['sh', script_file.name],
    preexec_fn=show_setting_pgrp,
)

print('PARENT: Pausing before signaling {}...'.format(proc.pid))
sys.stdout.flush()
time.sleep(1)
print('PARENT: Signaling process group {}'.format(proc.pid))
os.killpg(proc.pid, signal.SIGUSR1)
time.sleep(3)

"""
The sequence of events is
    The parent program instantiates Popen.
    The Popen instance forks a new process.
    The new process runs os.setpgrp().
    The new process runs exec() to start the shell.
    The shell runs the shell script.
    The shell script forks again and that process execs Python.
    Python runs signal_child.py.
    The parent program signals the process group using the pid of the shell.
    The shell and Python processes receive the signal.
    The shell ignores the signal.
    The Python process running signal_child.py invokes the signal handler.
"""
