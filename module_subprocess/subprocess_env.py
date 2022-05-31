import os
import subprocess
import time


def run(cmd=None):
    if cmd is None:
        return {"msg": "no cmd"}
    p = subprocess.Popen(cmd, shell=True)
    while p.poll() is None:
        print("running...")
        time.sleep(0.5)

    return_code = p.returncode
    return {"return_code": return_code}


if __name__ == "__main__":
    cmd_1 = "echo helloworld"
    run(cmd_1)

    cmd_2 = "echo $PATH"
    run(cmd_2)

    cmd_3 = "echo $MY_VAR !!!"
    run(cmd_3)

    os.environ["MY_VAR"] = "this is my var"
    run(cmd_3)
