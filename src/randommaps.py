import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.mapinfo import MapInfo


@dataclass
class RandomMaps(GenieClass):
    random_map_count: int
    random_maps_ptr: int
    map_info_1: list[MapInfo]
    map_info_2: list[MapInfo]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        random_map_count = content.read_int_32(signed=False)
        random_maps_ptr = content.read_int_32()
        map_info_1 = content.read_class_array(MapInfo, random_map_count)
        map_info_2 = content.read_class_array(MapInfo, random_map_count)
        return cls(
            random_map_count=random_map_count,
            random_maps_ptr=random_maps_ptr,
            map_info_1=map_info_1,
            map_info_2=map_info_2,
        )
