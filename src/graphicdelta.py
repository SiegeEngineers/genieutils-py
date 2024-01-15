from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class GraphicDelta(ByteHandler):
    graphic_id: int
    padding_1: int
    sprite_ptr: int
    offset_x: int
    offset_y: int
    display_angle: int
    padding_2: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.graphic_id = self.read_int_16()
        self.padding_1 = self.read_int_16()
        self.sprite_ptr = self.read_int_32()
        self.offset_x = self.read_int_16()
        self.offset_y = self.read_int_16()
        self.display_angle = self.read_int_16()
        self.padding_2 = self.read_int_16()
