import fileinput
import glob
import sys

if __name__ == "__main__":
    from_base = sys.argv[1]
    to_base = sys.argv[2]
    files = sys.argv[3:]

    for line in fileinput.input(files, inplace=True):
        if fileinput.isfirstline():
            sys.stderr.write("Started processing {}\n".format(fileinput.filename()))
            sys.stderr.write(
                "Directory contains: {}\n".format(glob.glob("etc_hosts.txt*"))
            )
        line = line.rstrip().replace(from_base, to_base)
        print(line)

    sys.stderr.write("Finished processing\n")
    sys.stderr.write("Directory contains: {}\n".format(glob.glob("etc_hosts.txt*")))
