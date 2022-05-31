from zipfile_infolist import print_info
import zipfile


with zipfile.ZipFile("write_arcname.zip", mode="w") as zf:
    zf.write("README.txt", arcname="NOT_README.txt")

print_info("write_arcname.zip")
