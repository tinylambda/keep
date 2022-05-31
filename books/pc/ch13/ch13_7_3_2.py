import shutil


try:
    shutil.copytree("tmp", "/tmp")
except shutil.Error as e:
    for src, dst, msg in e.args[0]:
        print(dst, src, msg)
