#! /usr/bin/env python3
import dataclasses
import json
import zlib
from pathlib import Path

from src.datfile import DatFile

DAT = Path(__file__).with_name('empires2_x2_p1.dat')#.parent / 'pompeii' / 'empires2_x2_p1.dat'
DECOMPRESSED_DAT = Path(__file__).with_name('empires2_x2_p1.decompressed.dat')
OUT = Path(__file__).with_name('empires2_x2_p1.reconstructed.dat')


def main():
    content = DAT.read_bytes()
    decompressed = zlib.decompress(content, wbits=-15)
    DECOMPRESSED_DAT.write_bytes(decompressed)
    # decompressed = DECOMPRESSED_DAT.read_bytes()
    # dat_file = DatFile(memoryview(decompressed))
    dat_file = DatFile.parse(DAT)
    re_encoded = dat_file.to_bytes()
    OUT.write_bytes(re_encoded)
    # print(json.dumps(dataclasses.asdict(dat_file), indent=2))
    for i in range(len(re_encoded)):
        if decompressed[i] != re_encoded[i]:
            print(f'disparity at {i}/{len(decompressed)} ({(100*i/len(decompressed)):.2f} %)')
            raise SystemExit
    print('all gud so far')
    assert len(decompressed) == len(re_encoded)
    assert decompressed == re_encoded
    print('done')


if __name__ == '__main__':
    main()
