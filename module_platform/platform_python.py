import platform


if __name__ == "__main__":
    print("Version: ", platform.python_version())
    print("Version tuple: ", platform.python_version_tuple())
    print("Compiler: ", platform.python_compiler())
    print("Build: ", platform.python_build())
