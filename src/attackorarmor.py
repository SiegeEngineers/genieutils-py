import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class AttackOrArmor(GenieClass):
    class_: int
    amount: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        return cls(
            class_=content.read_int_16(),
            amount=content.read_int_16(),
        )
