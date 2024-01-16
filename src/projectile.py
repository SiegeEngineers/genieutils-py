from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class Projectile(ByteHandler):
    projectile_type: int
    smart_mode: int
    hit_mode: int
    vanish_mode: int
    area_effect_specials: int
    projectile_arc: float

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.projectile_type = self.read_int_8()
        self.smart_mode = self.read_int_8()
        self.hit_mode = self.read_int_8()
        self.vanish_mode = self.read_int_8()
        self.area_effect_specials = self.read_int_8()
        self.projectile_arc = self.read_float()
