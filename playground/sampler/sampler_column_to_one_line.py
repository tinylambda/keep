import sys
import pandas


if __name__ == "__main__":
    csv_filename = sys.argv[1]
    colname = sys.argv[2]
    df = pandas.read_csv(csv_filename, skiprows=0)
    print(df, type(df))
    print(df[colname], type(colname))
    # normal
    print(", ".join(map(str, df[colname])))
    print("-" * 64)
    # as string literals
    print(", ".join(f"'{item}'" for item in df[colname]))
