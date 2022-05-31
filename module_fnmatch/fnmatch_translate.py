import fnmatch


pattern = "fnmatch_*.py"
print("Pattern: ", pattern)
print("Regex: ", fnmatch.translate(pattern))
