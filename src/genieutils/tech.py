from dataclasses import dataclass

from genieutils.common import ByteHandler, GenieClass


@dataclass
class ResearchResourceCost(GenieClass):
    type: int
    amount: int
    flag: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'ResearchResourceCost':
        return cls(
            type=content.read_int_16(),
            amount=content.read_int_16(),
            flag=content.read_int_8(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.type),
            self.write_int_16(self.amount),
            self.write_int_8(self.flag),
        ])


@dataclass
class Tech(GenieClass):
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

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Tech':
        return cls(
            required_techs=content.read_int_16_array(6),
            resource_costs=content.read_class_array(ResearchResourceCost, 3),
            required_tech_count=content.read_int_16(),
            civ=content.read_int_16(),
            full_tech_mode=content.read_int_16(),
            research_location=content.read_int_16(),
            language_dll_name=content.read_int_32(),
            language_dll_description=content.read_int_32(),
            research_time=content.read_int_16(),
            effect_id=content.read_int_16(),
            type=content.read_int_16(),
            icon_id=content.read_int_16(),
            button_id=content.read_int_8(),
            language_dll_help=content.read_int_32(),
            language_dll_tech_tree=content.read_int_32(),
            hot_key=content.read_int_32(),
            name=content.read_debug_string(),
            repeatable=content.read_int_8(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16_array(self.required_techs),
            self.write_class_array(self.resource_costs),
            self.write_int_16(self.required_tech_count),
            self.write_int_16(self.civ),
            self.write_int_16(self.full_tech_mode),
            self.write_int_16(self.research_location),
            self.write_int_32(self.language_dll_name),
            self.write_int_32(self.language_dll_description),
            self.write_int_16(self.research_time),
            self.write_int_16(self.effect_id),
            self.write_int_16(self.type),
            self.write_int_16(self.icon_id),
            self.write_int_8(self.button_id),
            self.write_int_32(self.language_dll_help),
            self.write_int_32(self.language_dll_tech_tree),
            self.write_int_32(self.hot_key),
            self.write_debug_string(self.name),
            self.write_int_8(self.repeatable),
        ])
