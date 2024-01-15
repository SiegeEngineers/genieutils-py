from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class SoundItem(ByteHandler):
    filename: str
    resource_id: int
    probability: int
    civilization: int
    icon_set: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.filename = self.read_debug_string()
        self.resource_id = self.read_int_32()
        self.probability = self.read_int_16()
        self.civilization = self.read_int_16()
        self.icon_set = self.read_int_16()
