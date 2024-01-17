import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class MapElevation(GenieClass):
    proportion: int
    terrain: int
    clump_count: int
    base_terrain: int
    base_elevation: int
    tile_spacing: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        return cls(
            proportion=content.read_int_32(),
            terrain=content.read_int_32(),
            clump_count=content.read_int_32(),
            base_terrain=content.read_int_32(),
            base_elevation=content.read_int_32(),
            tile_spacing=content.read_int_32(),
        )
