from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class EffectCommand(GenieClass):
    type: int
    a: int
    b: int
    c: int
    d: float

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'EffectCommand':
        return cls(
            type=content.read_int_8(),
            a=content.read_int_16(),
            b=content.read_int_16(),
            c=content.read_int_16(),
            d=content.read_float(),
        )
