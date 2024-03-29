import filecmp
import pprint


dc = filecmp.dircmp("example/dir1", "example/dir2")
print("Common: ")
pprint.pprint(dc.common)

print("\nDirectories: ")
pprint.pprint(dc.common_dirs)

print("\nFiles: ")
pprint.pprint(dc.common_dirs)

print("\nFunny: ")
pprint.pprint(dc.common_funny)
