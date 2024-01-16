from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class ResourceStorage(ByteHandler):
    type: int
    amount: float
    flag: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.type = self.read_int_16()
        self.amount = self.read_float()
        self.flag = self.read_int_8()
