import typing
from dataclasses import dataclass

from src.buildingannex import BuildingAnnex
from src.common import ByteHandler, GenieClass


@dataclass
class Building(GenieClass):
    construction_graphic_id: int
    snow_graphic_id: int
    destruction_graphic_id: int
    destruction_rubble_graphic_id: int
    researching_graphic: int
    research_completed_graphic: int
    adjacent_mode: int
    graphics_angle: int
    disappears_when_built: int
    stack_unit_id: int
    foundation_terrain_id: int
    old_overlap_id: int
    tech_id: int
    can_burn: int
    annexes: list[BuildingAnnex]
    head_unit: int
    transform_unit: int
    transform_sound: int
    construction_sound: int
    wwise_transform_sound_id: int
    wwise_construction_sound_id: int
    garrison_type: int
    garrison_heal_rate: float
    garrison_repair_rate: float
    pile_unit: int
    looting_table: list[int]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Building':
        return cls(
            construction_graphic_id=content.read_int_16(),
            snow_graphic_id=content.read_int_16(),
            destruction_graphic_id=content.read_int_16(),
            destruction_rubble_graphic_id=content.read_int_16(),
            researching_graphic=content.read_int_16(),
            research_completed_graphic=content.read_int_16(),
            adjacent_mode=content.read_int_8(),
            graphics_angle=content.read_int_16(),
            disappears_when_built=content.read_int_8(),
            stack_unit_id=content.read_int_16(),
            foundation_terrain_id=content.read_int_16(),
            old_overlap_id=content.read_int_16(),
            tech_id=content.read_int_16(),
            can_burn=content.read_int_8(),
            annexes=content.read_class_array(BuildingAnnex, 4),
            head_unit=content.read_int_16(),
            transform_unit=content.read_int_16(),
            transform_sound=content.read_int_16(),
            construction_sound=content.read_int_16(),
            wwise_transform_sound_id=content.read_int_32(),
            wwise_construction_sound_id=content.read_int_32(),
            garrison_type=content.read_int_8(),
            garrison_heal_rate=content.read_float(),
            garrison_repair_rate=content.read_float(),
            pile_unit=content.read_int_16(),
            looting_table=content.read_int_8_array(6),
        )
