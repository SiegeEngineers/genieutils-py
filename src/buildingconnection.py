import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.techtreecommon import Common


@dataclass
class BuildingConnection(GenieClass):
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

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        id = content.read_int_32()
        status = content.read_int_8()
        buildings_count = content.read_int_8()
        buildings = content.read_int_32_array(buildings_count)
        units_count = content.read_int_8()
        units = content.read_int_32_array(units_count)
        techs_count = content.read_int_8()
        techs = content.read_int_32_array(techs_count)
        common = content.read_class(Common)
        location_in_age = content.read_int_8()
        units_techs_total = content.read_int_8_array(5)
        units_techs_first = content.read_int_8_array(5)
        line_mode = content.read_int_32()
        enabling_research = content.read_int_32()
        return cls(
            id=id,
            status=status,
            buildings_count=buildings_count,
            buildings=buildings,
            units_count=units_count,
            units=units,
            techs_count=techs_count,
            techs=techs,
            common=common,
            location_in_age=location_in_age,
            units_techs_total=units_techs_total,
            units_techs_first=units_techs_first,
            line_mode=line_mode,
            enabling_research=enabling_research,
        )
