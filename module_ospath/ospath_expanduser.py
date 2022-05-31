import os.path

if __name__ == "__main__":
    for user in ["", "dhellmann", "nosuchuser"]:
        lookup = "~" + user
        print("{!r:>15} : {!r}".format(lookup, os.path.expanduser(lookup)))
