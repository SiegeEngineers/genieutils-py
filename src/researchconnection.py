from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.techtreecommon import Common


@dataclass
class ResearchConnection(GenieClass):
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

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'ResearchConnection':
        id_ = content.read_int_32()
        status = content.read_int_8()
        upper_building = content.read_int_32()
        buildings_count = content.read_int_8()
        buildings = content.read_int_32_array(buildings_count)
        units_count = content.read_int_8()
        units = content.read_int_32_array(units_count)
        techs_count = content.read_int_8()
        techs = content.read_int_32_array(techs_count)
        common = content.read_class(Common)
        vertical_line = content.read_int_32()
        location_in_age = content.read_int_32()
        line_mode = content.read_int_32()
        return cls(
            id=id_,
            status=status,
            upper_building=upper_building,
            buildings_count=buildings_count,
            buildings=buildings,
            units_count=units_count,
            units=units,
            techs_count=techs_count,
            techs=techs,
            common=common,
            vertical_line=vertical_line,
            location_in_age=location_in_age,
            line_mode=line_mode,
        )
