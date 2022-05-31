import sys


class NoisyImportFinder:
    PATH_TRIGGER = "NoisyImportFinder_PATH_TRIGGER"

    def __init__(self, path_entry):
        print("Checking {}: ".format(path_entry), end=" ")
        if path_entry != self.PATH_TRIGGER:
            print("Wrong finder")
            raise ImportError()
        else:
            print("Works")

    def find_module(self, fullname, path=None):
        print("Looking for {!r}".format(fullname))


sys.path_hooks.append(NoisyImportFinder)

for hook in sys.path_hooks:
    print("Path hook: {}".format(hook))

sys.path.insert(0, NoisyImportFinder.PATH_TRIGGER)

try:
    print("Importing target_module")
    import target_module
except Exception as e:
    print("Import failed: ", e)
