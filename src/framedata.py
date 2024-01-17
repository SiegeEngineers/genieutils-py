import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class FrameData(GenieClass):
    frame_count: int
    angle_count: int
    shape_id: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        return cls(
            frame_count=content.read_int_16(),
            angle_count=content.read_int_16(),
            shape_id=content.read_int_16(),
        )
