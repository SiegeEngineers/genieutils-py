from enum import IntEnum

from src.datatypes import Int, Float, String

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
        if tmp_size != 0x0A60:
            pass
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

    def read_float(self):
        return Float.from_bytes(self.consume_range(4))

    def read_float_array(self, size: int) -> list[float]:
        elements = []
        for i in range(size):
            elements.append(self.read_float())
        return elements
