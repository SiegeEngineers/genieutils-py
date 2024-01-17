import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class ResourceStorage(GenieClass):
    type: int
    amount: float
    flag: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'ResourceStorage':
        return cls(
            type=content.read_int_16(),
            amount=content.read_float(),
            flag=content.read_int_8(),
        )
