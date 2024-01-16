#! /usr/bin/env python3
import dataclasses
import json
from pathlib import Path

from src.datfile import DatFile

DAT = Path(__file__).with_name('empires2_x2_p1.dat')
DECOMPRESSED_DAT = Path(__file__).with_name('empires2_x2_p1.decompressed.dat')


def main():
    # content = DAT.read_bytes()
    # decompressed = zlib.decompress(content, wbits=-15)
    decompressed = DECOMPRESSED_DAT.read_bytes()
    dat_file = DatFile(memoryview(decompressed))
    print(json.dumps(dataclasses.asdict(dat_file), indent=2))


if __name__ == '__main__':
    main()
