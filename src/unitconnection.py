import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.techtreecommon import Common


@dataclass
class UnitConnection(GenieClass):
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

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'UnitConnection':
        id = content.read_int_32()
        status = content.read_int_8()
        upper_building = content.read_int_32()
        common = content.read_class(Common)
        vertical_line = content.read_int_32()
        units_count = content.read_int_8()
        units = content.read_int_32_array(units_count)
        location_in_age = content.read_int_32()
        required_research = content.read_int_32()
        line_mode = content.read_int_32()
        enabling_research = content.read_int_32()
        return cls(
            id=id,
            status=status,
            upper_building=upper_building,
            common=common,
            vertical_line=vertical_line,
            units_count=units_count,
            units=units,
            location_in_age=location_in_age,
            required_research=required_research,
            line_mode=line_mode,
            enabling_research=enabling_research,
        )
