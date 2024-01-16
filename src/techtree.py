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
        self.tech_tree_ages = self.read_tech_tree_age_array(self.age_count)
        self.building_connections = self.read_building_connection_array(self.building_count)
        self.unit_connections = self.read_unit_connection_array(self.unit_count)
        self.research_connections = self.read_research_connection_array(self.research_count)

    def read_tech_tree_age_array(self, size: int) -> list[TechTreeAge]:
        elements = []
        for i in range(size):
            tech_tree_age = TechTreeAge(self.content[self.offset:])
            elements.append(tech_tree_age)
            self.offset += tech_tree_age.offset
        return elements

    def read_building_connection_array(self, size: int) -> list[BuildingConnection]:
        elements = []
        for i in range(size):
            building_connection = BuildingConnection(self.content[self.offset:])
            elements.append(building_connection)
            self.offset += building_connection.offset
        return elements

    def read_unit_connection_array(self, size: int) -> list[UnitConnection]:
        elements = []
        for i in range(size):
            unit_connection = UnitConnection(self.content[self.offset:])
            elements.append(unit_connection)
            self.offset += unit_connection.offset
        return elements

    def read_research_connection_array(self, size: int) -> list[ResearchConnection]:
        elements = []
        for i in range(size):
            research_connection = ResearchConnection(self.content[self.offset:])
            elements.append(research_connection)
            self.offset += research_connection.offset
        return elements
