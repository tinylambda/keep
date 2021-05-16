import sys
import pandas


if __name__ == '__main__':
    filename = sys.argv[1]
    df = pandas.read_csv(filename, sep='\t')
    result = df.groupby(['orientationId'])['duration'].sum()
    print(result)
