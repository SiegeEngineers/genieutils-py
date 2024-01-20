from dataclasses import dataclass

from genieutils.common import ByteHandler, GenieClass


@dataclass
class Common(GenieClass):
    slots_used: int
    unit_research: tuple[int, int, int, int, int, int, int, int, int, int]
    mode: tuple[int, int, int, int, int, int, int, int, int, int]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Common':
        return cls(
            slots_used=content.read_int_32(),
            unit_research=content.read_int_32_array_10(),
            mode=content.read_int_32_array_10(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_32(self.slots_used),
            self.write_int_32_array(self.unit_research),
            self.write_int_32_array(self.mode),
        ])


@dataclass
class TechTreeAge(GenieClass):
    id: int
    status: int
    buildings: list[int]
    units: list[int]
    techs: list[int]
    common: Common
    num_building_levels: int
    buildings_per_zone: tuple[int, int, int, int, int, int, int, int, int, int]
    group_length_per_zone: tuple[int, int, int, int, int, int, int, int, int, int]
    max_age_length: int
    line_mode: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'TechTreeAge':
        id_ = content.read_int_32()
        status = content.read_int_8()
        buildings_count = content.read_int_8()
        buildings = content.read_int_32_array(buildings_count)
        units_count = content.read_int_8()
        units = content.read_int_32_array(units_count)
        techs_count = content.read_int_8()
        techs = content.read_int_32_array(techs_count)
        common = content.read_class(Common)
        num_building_levels = content.read_int_8()
        buildings_per_zone = content.read_int_8_array_10()
        group_length_per_zone = content.read_int_8_array_10()
        max_age_length = content.read_int_8()
        line_mode = content.read_int_32()
        return cls(
            id=id_,
            status=status,
            buildings=buildings,
            units=units,
            techs=techs,
            common=common,
            num_building_levels=num_building_levels,
            buildings_per_zone=buildings_per_zone,
            group_length_per_zone=group_length_per_zone,
            max_age_length=max_age_length,
            line_mode=line_mode,
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_32(self.id),
            self.write_int_8(self.status),
            self.write_int_8(len(self.buildings)),
            self.write_int_32_array(self.buildings),
            self.write_int_8(len(self.units)),
            self.write_int_32_array(self.units),
            self.write_int_8(len(self.techs)),
            self.write_int_32_array(self.techs),
            self.write_class(self.common),
            self.write_int_8(self.num_building_levels),
            self.write_int_8_array(self.buildings_per_zone),
            self.write_int_8_array(self.group_length_per_zone),
            self.write_int_8(self.max_age_length),
            self.write_int_32(self.line_mode),
        ])


@dataclass
class BuildingConnection(GenieClass):
    id: int
    status: int
    buildings: list[int]
    units: list[int]
    techs: list[int]
    common: Common
    location_in_age: int
    units_techs_total: tuple[int, int, int, int, int]
    units_techs_first: tuple[int, int, int, int, int]
    line_mode: int
    enabling_research: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'BuildingConnection':
        id_ = content.read_int_32()
        status = content.read_int_8()
        buildings_count = content.read_int_8()
        buildings = content.read_int_32_array(buildings_count)
        units_count = content.read_int_8()
        units = content.read_int_32_array(units_count)
        techs_count = content.read_int_8()
        techs = content.read_int_32_array(techs_count)
        common = content.read_class(Common)
        location_in_age = content.read_int_8()
        units_techs_total = content.read_int_8_array_5()
        units_techs_first = content.read_int_8_array_5()
        line_mode = content.read_int_32()
        enabling_research = content.read_int_32()
        return cls(
            id=id_,
            status=status,
            buildings=buildings,
            units=units,
            techs=techs,
            common=common,
            location_in_age=location_in_age,
            units_techs_total=units_techs_total,
            units_techs_first=units_techs_first,
            line_mode=line_mode,
            enabling_research=enabling_research,
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_32(self.id),
            self.write_int_8(self.status),
            self.write_int_8(len(self.buildings)),
            self.write_int_32_array(self.buildings),
            self.write_int_8(len(self.units)),
            self.write_int_32_array(self.units),
            self.write_int_8(len(self.techs)),
            self.write_int_32_array(self.techs),
            self.write_class(self.common),
            self.write_int_8(self.location_in_age),
            self.write_int_8_array(self.units_techs_total),
            self.write_int_8_array(self.units_techs_first),
            self.write_int_32(self.line_mode),
            self.write_int_32(self.enabling_research),
        ])


@dataclass
class UnitConnection(GenieClass):
    id: int
    status: int
    upper_building: int
    common: Common
    vertical_line: int
    units: list[int]
    location_in_age: int
    required_research: int
    line_mode: int
    enabling_research: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'UnitConnection':
        id_ = content.read_int_32()
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
            id=id_,
            status=status,
            upper_building=upper_building,
            common=common,
            vertical_line=vertical_line,
            units=units,
            location_in_age=location_in_age,
            required_research=required_research,
            line_mode=line_mode,
            enabling_research=enabling_research,
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_32(self.id),
            self.write_int_8(self.status),
            self.write_int_32(self.upper_building),
            self.write_class(self.common),
            self.write_int_32(self.vertical_line),
            self.write_int_8(len(self.units)),
            self.write_int_32_array(self.units),
            self.write_int_32(self.location_in_age),
            self.write_int_32(self.required_research),
            self.write_int_32(self.line_mode),
            self.write_int_32(self.enabling_research),
        ])


@dataclass
class ResearchConnection(GenieClass):
    id: int
    status: int
    upper_building: int
    buildings: list[int]
    units: list[int]
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
            buildings=buildings,
            units=units,
            techs=techs,
            common=common,
            vertical_line=vertical_line,
            location_in_age=location_in_age,
            line_mode=line_mode,
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_32(self.id),
            self.write_int_8(self.status),
            self.write_int_32(self.upper_building),
            self.write_int_8(len(self.buildings)),
            self.write_int_32_array(self.buildings),
            self.write_int_8(len(self.units)),
            self.write_int_32_array(self.units),
            self.write_int_8(len(self.techs)),
            self.write_int_32_array(self.techs),
            self.write_class(self.common),
            self.write_int_32(self.vertical_line),
            self.write_int_32(self.location_in_age),
            self.write_int_32(self.line_mode),
        ])


@dataclass
class TechTree(GenieClass):
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
            total_unit_tech_groups=total_unit_tech_groups,
            tech_tree_ages=tech_tree_ages,
            building_connections=building_connections,
            unit_connections=unit_connections,
            research_connections=research_connections,
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_8(len(self.tech_tree_ages)),
            self.write_int_8(len(self.building_connections)),
            self.write_int_8(len(self.unit_connections)),
            self.write_int_8(len(self.research_connections)),
            self.write_int_32(self.total_unit_tech_groups),
            self.write_class_array(self.tech_tree_ages),
            self.write_class_array(self.building_connections),
            self.write_class_array(self.unit_connections),
            self.write_class_array(self.research_connections),
        ])
