from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.unit import Unit


@dataclass
class Civ(GenieClass):
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

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Civ':
        player_type = content.read_int_8()
        name = content.read_debug_string()
        resources_size = content.read_int_16()
        tech_tree_id = content.read_int_16()
        team_bonus_id = content.read_int_16()
        resources = content.read_float_array(resources_size)
        icon_set = content.read_int_8()
        units_size = content.read_int_16()
        unit_pointers = content.read_int_32_array(units_size)
        units = content.read_class_array_with_pointers(Unit, units_size, unit_pointers)
        return cls(
            player_type=player_type,
            name=name,
            resources_size=resources_size,
            tech_tree_id=tech_tree_id,
            team_bonus_id=team_bonus_id,
            resources=resources,
            icon_set=icon_set,
            units_size=units_size,
            unit_pointers=unit_pointers,
            units=units,
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_8(self.player_type),
            self.write_debug_string(self.name),
            self.write_int_16(self.resources_size),
            self.write_int_16(self.tech_tree_id),
            self.write_int_16(self.team_bonus_id),
            self.write_float_array(self.resources),
            self.write_int_8(self.icon_set),
            self.write_int_16(self.units_size),
            self.write_int_32_array(self.unit_pointers),
            self.write_class_array_with_pointers(self.unit_pointers, self.units),
        ])
