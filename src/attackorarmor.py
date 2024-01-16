from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class AttackOrArmor(ByteHandler):
    class_: int
    amount: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.class_ = self.read_int_16()
        self.amount = self.read_int_16()
