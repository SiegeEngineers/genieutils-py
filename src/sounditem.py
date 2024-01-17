import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class SoundItem(GenieClass):
    filename: str
    resource_id: int
    probability: int
    civilization: int
    icon_set: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        return cls(
            filename=content.read_debug_string(),
            resource_id=content.read_int_32(),
            probability=content.read_int_16(),
            civilization=content.read_int_16(),
            icon_set=content.read_int_16(),
        )
