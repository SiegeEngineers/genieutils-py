import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class GraphicDelta(GenieClass):
    graphic_id: int
    padding_1: int
    sprite_ptr: int
    offset_x: int
    offset_y: int
    display_angle: int
    padding_2: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'GraphicDelta':
        return cls(
            graphic_id=content.read_int_16(),
            padding_1=content.read_int_16(),
            sprite_ptr=content.read_int_32(),
            offset_x=content.read_int_16(),
            offset_y=content.read_int_16(),
            display_angle=content.read_int_16(),
            padding_2=content.read_int_16(),
        )
