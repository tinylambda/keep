import subprocess


try:
    out_bytes = subprocess.check_output(["telnet", "arg1", "arg2"])
except subprocess.CalledProcessError as e:
    out_bytes = e.output
    code = e.returncode
    print(out_bytes, code)
except Exception as e:
    print("other exception", e)
