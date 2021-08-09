import gzip
import io
import glob
from concurrent import futures


def find_robots(filename):
    """find all of the hosts that access robots.txt in a single log file"""
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots(log_dir):
    """find all hosts across and entire sequence of files"""
    files = glob.glob(''.join([log_dir, '*.log.gz']))
    all_robots = set()
    with futures.ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots


if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)
