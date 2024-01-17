import typing
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
