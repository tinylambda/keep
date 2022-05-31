import tarfile

print("creating archive")
with tarfile.open("tarfile_add.tar", mode="w") as out:
    print("adding some file")
    out.add("tarfile_add.py")

print()
print("Contents: ")
with tarfile.open("tarfile_add.tar", mode="r") as t:
    for member_info in t.getmembers():
        print(member_info.name)
