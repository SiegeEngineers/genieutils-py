import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class Projectile(GenieClass):
    projectile_type: int
    smart_mode: int
    hit_mode: int
    vanish_mode: int
    area_effect_specials: int
    projectile_arc: float

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        return cls(
            projectile_type=content.read_int_8(),
            smart_mode=content.read_int_8(),
            hit_mode=content.read_int_8(),
            vanish_mode=content.read_int_8(),
            area_effect_specials=content.read_int_8(),
            projectile_arc=content.read_float(),
        )
