from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class FrameData(ByteHandler):
    frame_count: int
    angle_count: int
    shape_id: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.frame_count = self.read_int_16()
        self.angle_count = self.read_int_16()
        self.shape_id = self.read_int_16()
