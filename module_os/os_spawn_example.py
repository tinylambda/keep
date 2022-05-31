import os

if __name__ == "__main__":
    os.spawnlp(os.P_WAIT, "pwd", "pwd", "-P")
