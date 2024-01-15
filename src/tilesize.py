from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class TileSize(ByteHandler):
    width: int
    height: int
    delta_y: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.width = self.read_int_16()
        self.height = self.read_int_16()
        self.delta_y = self.read_int_16()
