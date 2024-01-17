import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class Common(GenieClass):
    slots_used: int
    unit_research: list[int]
    mode: list[int]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        return cls(
            slots_used=content.read_int_32(),
            unit_research=content.read_int_32_array(10),
            mode=content.read_int_32_array(10),
        )
