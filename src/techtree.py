from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class Common(GenieClass):
    slots_used: int
    unit_research: list[int]
    mode: list[int]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Common':
        return cls(
            slots_used=content.read_int_32(),
            unit_research=content.read_int_32_array(10),
            mode=content.read_int_32_array(10),
        )


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
    def from_bytes(cls, content: ByteHandler) -> 'TechTreeAge':
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
    def from_bytes(cls, content: ByteHandler) -> 'BuildingConnection':
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


@dataclass
class TechTree(GenieClass):
    age_count: int
    building_count: int
    unit_count: int
    research_count: int
    total_unit_tech_groups: int
    tech_tree_ages: list[TechTreeAge]
    building_connections: list[BuildingConnection]
    unit_connections: list[UnitConnection]
    research_connections: list[ResearchConnection]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'TechTree':
        age_count = content.read_int_8()
        building_count = content.read_int_8()
        unit_count = content.read_int_8()
        research_count = content.read_int_8()
        total_unit_tech_groups = content.read_int_32()
        tech_tree_ages = content.read_class_array(TechTreeAge, age_count)
        building_connections = content.read_class_array(BuildingConnection, building_count)
        unit_connections = content.read_class_array(UnitConnection, unit_count)
        research_connections = content.read_class_array(ResearchConnection, research_count)
        return cls(
            age_count=age_count,
            building_count=building_count,
            unit_count=unit_count,
            research_count=research_count,
            total_unit_tech_groups=total_unit_tech_groups,
            tech_tree_ages=tech_tree_ages,
            building_connections=building_connections,
            unit_connections=unit_connections,
            research_connections=research_connections,
        )
