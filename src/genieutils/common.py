from abc import ABC
from enum import IntEnum
from typing import TypeVar

from genieutils.datatypes import Int, Float, String

TILE_TYPE_COUNT = 19
TERRAIN_COUNT = 200
TERRAIN_UNITS_SIZE = 30


class UnitType(IntEnum):
    EyeCandy = 10
    Trees = 15
    Flag = 20
    DeadFish = 30
    Bird = 40
    Combatant = 50
    Projectile = 60
    Creatable = 70
    Building = 80
    AoeTrees = 90


class GenieClass(ABC):
    @classmethod
    def from_bytes(cls, data: 'ByteHandler'):
        raise NotImplementedError

    @classmethod
    def from_bytes_with_count(cls, data: 'ByteHandler', terrains_used_1: int):
        raise NotImplementedError

    def to_bytes(self) -> bytes:
        raise NotImplementedError

    def write_debug_string(self, value: str) -> bytes:
        return (self.write_int_16(0x0A60, signed=False)
                + self.write_int_16(len(value), signed=False)
                + value.encode('utf-8'))

    def write_string(self, length: int, value: str) -> bytes:
        return String.to_bytes(value, length)

    def write_int_8(self, value: int) -> bytes:
        return Int.to_bytes(value, length=1, signed=False)

    def write_int_8_array(self, value: list[int]) -> bytes:
        return b''.join(self.write_int_8(v) for v in value)

    def write_int_16(self, value: int, signed=True) -> bytes:
        return Int.to_bytes(value, length=2, signed=signed)

    def write_int_16_array(self, value: list[int]) -> bytes:
        return b''.join(self.write_int_16(v) for v in value)

    def write_int_32(self, value: int, signed=True) -> bytes:
        return Int.to_bytes(value, length=4, signed=signed)

    def write_int_32_array(self, value: list[int]) -> bytes:
        return b''.join(self.write_int_32(v) for v in value)

    def write_float(self, value: float) -> bytes:
        return Float.to_bytes(value)

    def write_float_array(self, value: list[float]) -> bytes:
        return b''.join(self.write_float(v) for v in value)

    def write_class(self, value: 'GenieClass') -> bytes:
        retval = value.to_bytes()
        if retval:
            return retval
        return b''

    def write_class_array(self, value: list['GenieClass']) -> bytes:
        retval = b''.join(self.write_class(v) for v in value)
        if retval:
            return retval
        return b''

    def write_class_array_with_pointers(self, pointers: list[int], value: list['GenieClass']) -> bytes:
        retval = b''.join(self.write_class(v) for i, v in enumerate(value) if pointers[i])
        if retval:
            return retval
        return b''


C = TypeVar('C', bound=GenieClass)


class ByteHandler:
    def __init__(self, content: memoryview):
        self.content = content
        self.offset = 0

    def consume_range(self, length: int) -> memoryview:
        start = self.offset
        end = start + length
        self.offset = end
        return self.content[start:end]

    def read_debug_string(self) -> str:
        tmp_size = self.read_int_16(signed=False)
        assert tmp_size == 0x0A60
        size = self.read_int_16(signed=False)
        return String.from_bytes(self.consume_range(size))

    def read_string(self, length: int) -> str:
        return String.from_bytes(self.consume_range(length))

    def read_int_8(self) -> int:
        return Int.from_bytes(self.consume_range(1), signed=False)

    def read_int_8_array(self, size: int) -> list[int]:
        elements = []
        for i in range(size):
            elements.append(self.read_int_8())
        return elements

    def read_int_16(self, signed=True) -> int:
        return Int.from_bytes(self.consume_range(2), signed=signed)

    def read_int_16_array(self, size: int) -> list[int]:
        elements = []
        for i in range(size):
            elements.append(self.read_int_16())
        return elements

    def read_int_32(self, signed=True) -> int:
        return Int.from_bytes(self.consume_range(4), signed=signed)

    def read_int_32_array(self, size: int) -> list[int]:
        elements = []
        for i in range(size):
            elements.append(self.read_int_32())
        return elements

    def read_float(self) -> float:
        return Float.from_bytes(self.consume_range(4))

    def read_float_array(self, size: int) -> list[float]:
        elements = []
        for i in range(size):
            elements.append(self.read_float())
        return elements

    def read_class(self, class_: type[C]) -> C:
        element = class_.from_bytes(self)
        return element

    def read_class_array(self, class_: type[C], size: int) -> list[C]:
        elements = []
        for i in range(size):
            element = class_.from_bytes(self)
            elements.append(element)
        return elements

    def read_class_array_with_pointers(self, class_: type[C], size: int, pointers: list[int]) -> list[C | None]:
        elements = []
        for i in range(size):
            element = None
            if pointers[i]:
                element = class_.from_bytes(self)
            elements.append(element)
        return elements

    def read_class_array_with_param(self, class_: type[C], size: int, terrains_used_1: int) -> list[C]:
        elements = []
        for i in range(size):
            terrain_restriction = class_.from_bytes_with_count(self, terrains_used_1)
            elements.append(terrain_restriction)
        return elements
