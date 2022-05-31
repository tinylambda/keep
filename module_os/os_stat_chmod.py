import os
import stat


if __name__ == "__main__":
    filename = "os_stat_chmod_example.txt"
    if os.path.exists(filename):
        os.unlink(filename)

    with open(filename, "wt") as f:
        f.write("contents")

    existing_permissions = stat.S_IMODE(os.stat(filename).st_mode)

    if not os.access(filename, os.X_OK):
        print("Adding execute permission")
        new_permissions = existing_permissions | stat.S_IXUSR
    else:
        print("Removing execute permission")
        new_permissions = existing_permissions ^ stat.S_IXUSR

    os.chmod(filename, new_permissions)
