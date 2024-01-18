#! /usr/bin/env python3
import argparse
import dataclasses
import json
from pathlib import Path

from genieutils.datfile import DatFile


def dat_to_json():
    parser = argparse.ArgumentParser(
        prog='dat-to-json',
        description='Read a genie engine dat file and print the json representation to stdout',
    )
    parser.add_argument('filename', type=Path, help='The dat file to read')
    args = parser.parse_args()

    dat_file = DatFile.parse(args.filename)
    print(json.dumps(dataclasses.asdict(dat_file), indent=2))


def main():
    dat_to_json()


if __name__ == '__main__':
    main()
