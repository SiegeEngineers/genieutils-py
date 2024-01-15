from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class EffectCommand(ByteHandler):
    type: int
    a: int
    b: int
    c: int
    d: float

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.type = self.read_int_8()
        self.a = self.read_int_16()
        self.b = self.read_int_16()
        self.c = self.read_int_16()
        self.d = self.read_float()
