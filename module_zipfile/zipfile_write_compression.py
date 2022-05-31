from zipfile_infolist import print_info
import zipfile

try:
    import zlib

    compression = zipfile.ZIP_DEFLATED
except (ImportError, AttributeError):
    compression = zipfile.ZIP_STORED

modes = {
    zipfile.ZIP_DEFLATED: "deflated",
    zipfile.ZIP_STORED: "stored",
}

print("creating archive")
with zipfile.ZipFile("write_compression.zip", mode="w") as zf:
    mode_name = modes[compression]
    added_filename = "README.txt"
    print(f"adding {added_filename} with compression mode", mode_name)
    zf.write(added_filename, compress_type=compression)

print()
print_info("write_compression.zip")
