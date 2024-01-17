import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.techtreecommon import Common


@dataclass
class TechTreeAge(GenieClass):
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
        num_building_levels = content.read_int_8()
        buildings_per_zone = content.read_int_8_array(10)
        group_length_per_zone = content.read_int_8_array(10)
        max_age_length = content.read_int_8()
        line_mode = content.read_int_32()
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
            num_building_levels=num_building_levels,
            buildings_per_zone=buildings_per_zone,
            group_length_per_zone=group_length_per_zone,
            max_age_length=max_age_length,
            line_mode=line_mode,
        )
