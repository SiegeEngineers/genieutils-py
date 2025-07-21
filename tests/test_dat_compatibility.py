import zlib
from pathlib import Path

import pytest

from genieutils.common import ByteHandler
from genieutils.datfile import DatFile

TESTDATA_DIR = Path(__file__).with_name('testdata')


class TestDatCompatibility:
    def test_there_are_actually_dat_files_for_testing(self):
        assert len(list(TESTDATA_DIR.rglob('*.dat')))

    @pytest.mark.parametrize('datfile', sorted(TESTDATA_DIR.rglob('*.dat'), reverse=True))
    def test_compatibility_with_dat_files(self, datfile: Path):
        version, data = self.get_version(datfile)
        print(datfile)
        print(version)
        if version in ('VER 8.8', 'VER 8.4', 'VER 7.8', 'VER 7.7'):
            byte_handler = ByteHandler(memoryview(data))
            content = DatFile.from_bytes(byte_handler)
            re_encoded = content.to_bytes()
            index = 0
            for data_byte, re_encoded_byte in zip(data, re_encoded):
                if data_byte != re_encoded_byte:
                    raise Exception(f'Mismatch at byte {index}: {data_byte=} {re_encoded_byte=}')
                index += 1
            if len(data) != len(re_encoded):
                raise Exception(f'Length Mismatch: {len(data)} vs. {len(re_encoded)}')
        else:
            pytest.skip(f'version {version} is currently not supported')

    def get_version(self, datfile: Path) -> tuple[str, bytes]:
        content = datfile.read_bytes()
        data = zlib.decompress(content, wbits=-15)
        version = data[:8].rstrip(b'\0').decode()
        return version, data
