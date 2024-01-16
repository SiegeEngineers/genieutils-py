from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class DamageGraphic(ByteHandler):
    graphic_id: int
    damage_percent: int
    apply_mode: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.graphic_id = self.read_int_16()
        self.damage_percent = self.read_int_16()
        self.apply_mode = self.read_int_8()
