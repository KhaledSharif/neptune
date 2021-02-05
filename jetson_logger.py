from jtop import jtop
from time import sleep
from os.path import exists
from datetime import datetime, timedelta
import argparse

def convert_types(x) -> str:
    if isinstance(x, datetime):
        return str(x.timestamp())

    if isinstance(x, timedelta):
        return str(x.total_seconds())
    
    return str(x)

def main(path_to_mutex):
    if exists(path_to_mutex):
        print("Error: mutex already present when launching logger")
        exit(1)

    columns = None

    with jtop() as jetson:
        # jetson.ok() will provide the proper update frequency
        while jetson.ok():
            if exists(path_to_mutex):
                break

            statistics_dict = jetson.stats

            if columns is None:
                columns = sorted(list(statistics_dict.keys()))
                print(",".join(columns))

            statistics_row = [convert_types(statistics_dict[column_name]) for column_name in columns]

            print(",".join(statistics_row))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="log jetson statistics to stdout until a special mutex file is created")

    parser.add_argument(
        "--mutex",
        type=str,
        help="path to a non-existent file that will turn off this logger when created",
        required=True)

    args = parser.parse_args()
    
    main(args.mutex)