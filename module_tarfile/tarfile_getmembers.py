import tarfile
import time


with tarfile.open("/Users/Felix/Downloads/django.tar.gz", "r") as t:
    for member_info in t.getmembers():
        print(member_info.name)
        print(" Modified:", time.ctime(member_info.mtime))
        print(" Mode:", oct(member_info.mode))
        print(" Type:", member_info.type)
        print(" Size:", member_info.size, "bytes")
        print()
