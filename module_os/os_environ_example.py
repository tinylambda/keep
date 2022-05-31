import os


if __name__ == "__main__":
    print(f'Initial value: {os.environ.get("TESTVAR", None)}')
    print("Child process:")
    os.system("echo $TESTVAR")

    os.environ["TESTVAR"] = "THIS VALUE WAS CHANGED"
    print()

    print(f'Changed value: {os.environ["TESTVAR"]}')
    print("Child process:")
    os.system("echo $TESTVAR")

    del os.environ["TESTVAR"]
    print()

    # Changes to os.environ are exported for child processes
    print(f'Removed value: {os.environ.get("TESTVAR", None)}')
    print("Child process:")
    os.system("echo $TESTVAR")
