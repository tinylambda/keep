import subprocess


if __name__ == "__main__":
    completed = subprocess.run(["ls", "-l"])
    print("returncode:", completed.returncode)
