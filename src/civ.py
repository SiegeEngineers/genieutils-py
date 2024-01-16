from dataclasses import dataclass

from src.common import ByteHandler
from src.unit import Unit


@dataclass
class Civ(ByteHandler):
    player_type: int
    name: str
    resources_size: int
    tech_tree_id: int
    team_bonus_id: int
    resources: list[float]
    icon_set: int
    units_size: int
    unit_pointers: list[int]
    units: list[Unit | None]

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.player_type = self.read_int_8()
        self.name = self.read_debug_string()
        self.resources_size = self.read_int_16()
        self.tech_tree_id = self.read_int_16()
        self.team_bonus_id = self.read_int_16()
        self.resources = self.read_float_array(self.resources_size)
        self.icon_set = self.read_int_8()
        self.units_size = self.read_int_16()
        self.unit_pointers = self.read_int_32_array(self.units_size)
        self.units = self.read_class_array_with_pointers(Unit, self.units_size, self.unit_pointers)
