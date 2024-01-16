from dataclasses import dataclass

from src.common import ByteHandler
from src.techtreecommon import Common


@dataclass
class BuildingConnection(ByteHandler):
    id: int
    status: int
    buildings_count: int
    buildings: list[int]
    units_count: int
    units: list[int]
    techs_count: int
    techs: list[int]
    common: Common
    location_in_age: int
    units_techs_total: list[int]
    units_techs_first: list[int]
    line_mode: int
    enabling_research: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.id = self.read_int_32()
        self.status = self.read_int_8()
        self.buildings_count = self.read_int_8()
        self.buildings = self.read_int_32_array(self.buildings_count)
        self.units_count = self.read_int_8()
        self.units = self.read_int_32_array(self.units_count)
        self.techs_count = self.read_int_8()
        self.techs = self.read_int_32_array(self.techs_count)
        self.common = self.read_common()
        self.location_in_age = self.read_int_8()
        self.units_techs_total = self.read_int_8_array(5)
        self.units_techs_first = self.read_int_8_array(5)
        self.line_mode = self.read_int_32()
        self.enabling_research = self.read_int_32()

    def read_common(self) -> Common:
        common = Common(self.content[self.offset:])
        self.offset += common.offset
        return common
