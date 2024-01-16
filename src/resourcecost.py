from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class ResourceCost(ByteHandler):
    type: int
    amount: int
    flag: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.type = self.read_int_16()
        self.amount = self.read_int_16()
        self.flag = self.read_int_16()
