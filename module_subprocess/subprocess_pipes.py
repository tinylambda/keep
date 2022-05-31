import subprocess


if __name__ == "__main__":
    cat = subprocess.Popen(
        ["cat", "subprocess_pipes.py"],
        stdout=subprocess.PIPE,
    )

    grep = subprocess.Popen(
        ["grep", "stdout"],
        stdin=cat.stdout,
        stdout=subprocess.PIPE,
    )

    cut = subprocess.Popen(
        ["cut", "-f", "3"],
        stdin=grep.stdout,
        stdout=subprocess.PIPE,
    )

    end_of_pipe = cut.stdout
    print("stdout lines:")
    for line in end_of_pipe:
        print(line.decode("utf8").strip())
