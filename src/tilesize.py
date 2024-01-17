import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class TileSize(GenieClass):
    width: int
    height: int
    delta_y: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'TileSize':
        return cls(
            width=content.read_int_16(),
            height=content.read_int_16(),
            delta_y=content.read_int_16(),
        )
