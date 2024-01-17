import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class BuildingAnnex(GenieClass):
    unit_id: int
    misplacement_x: float
    misplacement_y: float

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        return cls(
            unit_id=content.read_int_16(),
            misplacement_x=content.read_float(),
            misplacement_y=content.read_float(),
        )
