from dataclasses import dataclass

from src.common import ByteHandler
from src.techtreecommon import Common


@dataclass
class TechTreeAge(ByteHandler):
    id: int
    status: int
    buildings_count: int
    buildings: list[int]
    units_count: int
    units: list[int]
    techs_count: int
    techs: list[int]
    common: Common
    num_building_levels: int
    buildings_per_zone: list[int]
    group_length_per_zone: list[int]
    max_age_length: int
    line_mode: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.id = self.read_int_32()
        self.status = self.read_int_8()
        self.buildings_count = self.read_int_8()
        self.buildings = self.read_int_32_array(self.buildings_count)
        self.units_count = self.read_int_8()
        self.units = self.read_int_32_array(self.buildings_count)
        self.techs_count = self.read_int_8()
        self.techs = self.read_int_32_array(self.buildings_count)
        self.common = self.read_common()
        self.num_building_levels = self.read_int_8()
        self.buildings_per_zone = self.read_int_8_array(10)
        self.group_length_per_zone = self.read_int_8_array(10)
        self.max_age_length = self.read_int_8()
        self.line_mode = self.read_int_32()

    def read_common(self) -> Common:
        common = Common(self.content[self.offset:])
        self.offset += common.offset
        return common
