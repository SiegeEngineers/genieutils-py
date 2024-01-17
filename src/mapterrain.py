import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class MapTerrain(GenieClass):
    proportion: int
    terrain: int
    clump_count: int
    edge_spacing: int
    placement_terrain: int
    clumpiness: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        return cls(
            proportion=content.read_int_32(),
            terrain=content.read_int_32(),
            clump_count=content.read_int_32(),
            edge_spacing=content.read_int_32(),
            placement_terrain=content.read_int_32(),
            clumpiness=content.read_int_32(),
        )
