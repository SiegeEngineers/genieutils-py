from dataclasses import dataclass

from src.common import ByteHandler
from src.techtreecommon import Common


@dataclass
class UnitConnection(ByteHandler):
    id: int
    status: int
    upper_building: int
    common: Common
    vertical_line: int
    units_count: int
    units: list[int]
    location_in_age: int
    required_research: int
    line_mode: int
    enabling_research: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.id = self.read_int_32()
        self.status = self.read_int_8()
        self.upper_building = self.read_int_32()
        self.common = self.read_class(Common)
        self.vertical_line = self.read_int_32()
        self.units_count = self.read_int_8()
        self.units = self.read_int_32_array(self.units_count)
        self.location_in_age = self.read_int_32()
        self.required_research = self.read_int_32()
        self.line_mode = self.read_int_32()
        self.enabling_research = self.read_int_32()
