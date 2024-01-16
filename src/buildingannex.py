from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class BuildingAnnex(ByteHandler):
    unit_id: int
    misplacement_x: float
    misplacement_y: float

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.unit_id = self.read_int_16()
        self.misplacement_x = self.read_float()
        self.misplacement_y = self.read_float()
