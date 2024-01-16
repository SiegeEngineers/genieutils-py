from dataclasses import dataclass

from src.buildingconnection import BuildingConnection
from src.common import ByteHandler
from src.researchconnection import ResearchConnection
from src.techtreeage import TechTreeAge
from src.unitconnection import UnitConnection


@dataclass
class TechTree(ByteHandler):
    age_count: int
    building_count: int
    unit_count: int
    research_count: int
    total_unit_tech_groups: int
    tech_tree_ages: list[TechTreeAge]
    building_connections: list[BuildingConnection]
    unit_connections: list[UnitConnection]
    research_connections: list[ResearchConnection]

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.age_count = self.read_int_8()
        self.building_count = self.read_int_8()
        self.unit_count = self.read_int_8()
        self.research_count = self.read_int_8()
        self.total_unit_tech_groups = self.read_int_32()
        self.tech_tree_ages = self.read_class_array(TechTreeAge, self.age_count)
        self.building_connections = self.read_class_array(BuildingConnection, self.building_count)
        self.unit_connections = self.read_class_array(UnitConnection, self.unit_count)
        self.research_connections = self.read_class_array(ResearchConnection, self.research_count)
