import typing
from dataclasses import dataclass

from src.buildingconnection import BuildingConnection
from src.common import ByteHandler, GenieClass
from src.researchconnection import ResearchConnection
from src.techtreeage import TechTreeAge
from src.unitconnection import UnitConnection


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
