import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class DamageGraphic(GenieClass):
    graphic_id: int
    damage_percent: int
    apply_mode: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        return cls(
            graphic_id=content.read_int_16(),
            damage_percent=content.read_int_16(),
            apply_mode=content.read_int_8(),
        )
