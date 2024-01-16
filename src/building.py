from dataclasses import dataclass

from src.buildingannex import BuildingAnnex
from src.common import ByteHandler


@dataclass
class Building(ByteHandler):
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

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.construction_graphic_id = self.read_int_16()
        self.snow_graphic_id = self.read_int_16()
        self.destruction_graphic_id = self.read_int_16()
        self.destruction_rubble_graphic_id = self.read_int_16()
        self.researching_graphic = self.read_int_16()
        self.research_completed_graphic = self.read_int_16()
        self.adjacent_mode = self.read_int_8()
        self.graphics_angle = self.read_int_16()
        self.disappears_when_built = self.read_int_8()
        self.stack_unit_id = self.read_int_16()
        self.foundation_terrain_id = self.read_int_16()
        self.old_overlap_id = self.read_int_16()
        self.tech_id = self.read_int_16()
        self.can_burn = self.read_int_8()
        self.annexes = self.read_building_annex_array(4)
        self.head_unit = self.read_int_16()
        self.transform_unit = self.read_int_16()
        self.transform_sound = self.read_int_16()
        self.construction_sound = self.read_int_16()
        self.wwise_transform_sound_id = self.read_int_32()
        self.wwise_construction_sound_id = self.read_int_32()
        self.garrison_type = self.read_int_8()
        self.garrison_heal_rate = self.read_float()
        self.garrison_repair_rate = self.read_float()
        self.pile_unit = self.read_int_16()
        self.looting_table = self.read_int_8_array(6)

    def read_building_annex_array(self, size: int) -> list[BuildingAnnex]:
        elements = []
        for i in range(size):
            building_annex = BuildingAnnex(self.content[self.offset:])
            elements.append(building_annex)
            self.offset += building_annex.offset
        return elements
