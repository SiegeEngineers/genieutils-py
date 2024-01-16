from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class Common(ByteHandler):
    slots_used: int
    unit_research: list[int]
    mode: list[int]

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.slots_used = self.read_int_32()
        self.unit_research = self.read_int_32_array(10)
        self.mode = self.read_int_32_array(10)
