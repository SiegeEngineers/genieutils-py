import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class ResourceCost(GenieClass):
    type: int
    amount: int
    flag: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'ResourceCost':
        return cls(
            type=content.read_int_16(),
            amount=content.read_int_16(),
            flag=content.read_int_16(),
        )
