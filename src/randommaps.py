from dataclasses import dataclass

from src.common import ByteHandler
from src.mapinfo import MapInfo


@dataclass
class RandomMaps(ByteHandler):
    random_map_count: int
    random_maps_ptr: int
    map_info_1: list[MapInfo]
    map_info_2: list[MapInfo]

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.random_map_count = self.read_int_32(signed=False)
        self.random_maps_ptr = self.read_int_32()
        self.map_info_1 = self.read_map_info_array(self.random_map_count)
        self.map_info_2 = self.read_map_info_array(self.random_map_count)

    def read_map_info_array(self, size: int) -> list[MapInfo]:
        elements = []
        for i in range(size):
            map_info = MapInfo(self.content[self.offset:])
            elements.append(map_info)
            self.offset += map_info.offset
        return elements
