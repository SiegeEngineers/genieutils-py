from dataclasses import dataclass

from src.common import ByteHandler
from src.researchresourcecost import ResearchResourceCost


@dataclass
class Tech(ByteHandler):
    required_techs: list[int]
    resource_costs: list[ResearchResourceCost]
    required_tech_count: int
    civ: int
    full_tech_mode: int
    research_location: int
    language_dll_name: int
    language_dll_description: int
    research_time: int
    effect_id: int
    type: int
    icon_id: int
    button_id: int
    language_dll_help: int
    language_dll_tech_tree: int
    hot_key: int
    name: str
    repeatable: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.required_techs = self.read_int_16_array(6)
        self.resource_costs = self.read_class_array(ResearchResourceCost, 3)
        self.required_tech_count = self.read_int_16()
        self.civ = self.read_int_16()
        self.full_tech_mode = self.read_int_16()
        self.research_location = self.read_int_16()
        self.language_dll_name = self.read_int_32()
        self.language_dll_description = self.read_int_32()
        self.research_time = self.read_int_16()
        self.effect_id = self.read_int_16()
        self.type = self.read_int_16()
        self.icon_id = self.read_int_16()
        self.button_id = self.read_int_8()
        self.language_dll_help = self.read_int_32()
        self.language_dll_tech_tree = self.read_int_32()
        self.hot_key = self.read_int_32()
        self.name = self.read_debug_string()
        self.repeatable = self.read_int_8()
