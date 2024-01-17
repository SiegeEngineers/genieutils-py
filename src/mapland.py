import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class MapLand(GenieClass):
    land_id: int
    terrain: int
    land_spacing: int
    base_size: int
    zone: int
    placement_type: int
    padding_1: int
    base_x: int
    base_y: int
    land_proportion: int
    by_player_flag: int
    padding_2: int
    start_area_radius: int
    terrain_edge_fade: int
    clumpiness: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        return cls(
            land_id=content.read_int_32(),
            terrain=content.read_int_32(signed=False),
            land_spacing=content.read_int_32(),
            base_size=content.read_int_32(),
            zone=content.read_int_8(),
            placement_type=content.read_int_8(),
            padding_1=content.read_int_16(),
            base_x=content.read_int_32(),
            base_y=content.read_int_32(),
            land_proportion=content.read_int_8(),
            by_player_flag=content.read_int_8(),
            padding_2=content.read_int_16(),
            start_area_radius=content.read_int_32(),
            terrain_edge_fade=content.read_int_32(),
            clumpiness=content.read_int_32(),
        )
