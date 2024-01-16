from dataclasses import dataclass

from src.common import ByteHandler
from src.techtreecommon import Common


@dataclass
class ResearchConnection(ByteHandler):
    id: int
    status: int
    upper_building: int
    buildings_count: int
    buildings: list[int]
    units_count: int
    units: list[int]
    techs_count: int
    techs: list[int]
    common: Common
    vertical_line: int
    location_in_age: int
    line_mode: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.id = self.read_int_32()
        self.status = self.read_int_8()
        self.upper_building = self.read_int_32()
        self.buildings_count = self.read_int_8()
        self.buildings = self.read_int_32_array(self.buildings_count)
        self.units_count = self.read_int_8()
        self.units = self.read_int_32_array(self.units_count)
        self.techs_count = self.read_int_8()
        self.techs = self.read_int_32_array(self.techs_count)
        self.common = self.read_class(Common)
        self.vertical_line = self.read_int_32()
        self.location_in_age = self.read_int_32()
        self.line_mode = self.read_int_32()
