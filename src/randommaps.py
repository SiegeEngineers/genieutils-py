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
        self.map_info_1 = self.read_class_array(MapInfo, self.random_map_count)
        self.map_info_2 = self.read_class_array(MapInfo, self.random_map_count)
