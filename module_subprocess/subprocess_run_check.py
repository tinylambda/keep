import subprocess


if __name__ == "__main__":
    try:
        completed = subprocess.run(["false"], check=True)
        # completed = subprocess.run(['false'], check=False)
        # print(completed)
    except subprocess.CalledProcessError as err:
        print("ERROR:", err)
