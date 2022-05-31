import os


if __name__ == "__main__":
    print(f"Testing {__file__}")
    print(f"Exists: {os.access(__file__, os.F_OK)}")
    print(f"Readable: {os.access(__file__, os.R_OK)}")
    print(f"Writable: {os.access(__file__, os.W_OK)}")
    print(f"Executable: {os.access(__file__, os.X_OK)}")
