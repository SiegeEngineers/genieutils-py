from dataclasses import dataclass

from genieutils.common import ByteHandler, GenieClass
from genieutils.versions import Version


@dataclass(slots=True)
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

    def to_bytes(self, version: Version) -> bytes:
        return b''.join([
            self.write_int_16(self.type),
            self.write_int_16(self.amount),
            self.write_int_8(self.flag),
        ])


@dataclass(slots=True)
class ResearchLocation(GenieClass):
    location_id: int
    research_time: int
    button_id: int
    hot_key_id: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'ResearchLocation':
        return cls(
            location_id=content.read_int_16(),
            research_time=content.read_int_16(),
            button_id=content.read_int_8(),
            hot_key_id=content.read_int_32(),
        )

    def to_bytes(self, version: Version) -> bytes:
        return b''.join([
            self.write_int_16(self.location_id),
            self.write_int_16(self.research_time),
            self.write_int_8(self.button_id),
            self.write_int_32(self.hot_key_id),
        ])


@dataclass(slots=True)
class Tech(GenieClass):
    required_techs: tuple[int, int, int, int, int, int]
    resource_costs: tuple[ResearchResourceCost, ResearchResourceCost, ResearchResourceCost]
    required_tech_count: int
    civ: int
    full_tech_mode: int
    language_dll_name: int
    language_dll_description: int
    effect_id: int
    type: int
    icon_id: int
    language_dll_help: int
    language_dll_tech_tree: int
    name: str
    repeatable: int
    research_locations: list[ResearchLocation]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Tech':
        if content.version >= Version.VER_88:
            return cls.from_bytes_88(content)
        return cls.from_bytes_84(content)

    @classmethod
    def from_bytes_84(cls, content: ByteHandler) -> 'Tech':
        required_techs = content.read_int_16_array_6()
        resource_costs = content.read_class_array_3(ResearchResourceCost)
        required_tech_count = content.read_int_16()
        civ = content.read_int_16()
        full_tech_mode = content.read_int_16()
        research_location = content.read_int_16()
        language_dll_name = content.read_int_32()
        language_dll_description = content.read_int_32()
        research_time = content.read_int_16()
        effect_id = content.read_int_16()
        type = content.read_int_16()
        icon_id = content.read_int_16()
        button_id = content.read_int_8()
        language_dll_help = content.read_int_32()
        language_dll_tech_tree = content.read_int_32()
        hot_key = content.read_int_32()
        name = content.read_debug_string()
        repeatable = content.read_int_8()
        research_locations = [ResearchLocation(
            button_id=button_id,
            research_time=research_time,
            hot_key_id=hot_key,
            location_id=research_location,
        )]
        return cls(
            required_techs=required_techs,
            resource_costs=resource_costs,
            required_tech_count=required_tech_count,
            civ=civ,
            full_tech_mode=full_tech_mode,
            language_dll_name=language_dll_name,
            language_dll_description=language_dll_description,
            effect_id=effect_id,
            type=type,
            icon_id=icon_id,
            language_dll_help=language_dll_help,
            language_dll_tech_tree=language_dll_tech_tree,
            name=name,
            repeatable=repeatable,
            research_locations=research_locations,
        )

    @classmethod
    def from_bytes_88(cls, content: ByteHandler) -> 'Tech':
        required_techs = content.read_int_16_array_6()
        resource_costs = content.read_class_array_3(ResearchResourceCost)
        required_tech_count = content.read_int_16()
        civ = content.read_int_16()
        full_tech_mode = content.read_int_16()
        language_dll_name = content.read_int_32()
        language_dll_description = content.read_int_32()
        effect_id = content.read_int_16()
        type = content.read_int_16()
        icon_id = content.read_int_16()
        language_dll_help = content.read_int_32()
        language_dll_tech_tree = content.read_int_32()
        name = content.read_debug_string()
        repeatable = content.read_int_8()
        research_location_count = content.read_int_16()
        research_locations = content.read_class_array(ResearchLocation, research_location_count)
        return cls(
            required_techs=required_techs,
            resource_costs=resource_costs,
            required_tech_count=required_tech_count,
            civ=civ,
            full_tech_mode=full_tech_mode,
            language_dll_name=language_dll_name,
            language_dll_description=language_dll_description,
            effect_id=effect_id,
            type=type,
            icon_id=icon_id,
            language_dll_help=language_dll_help,
            language_dll_tech_tree=language_dll_tech_tree,
            name=name,
            repeatable=repeatable,
            research_locations=research_locations,
        )

    def to_bytes(self, version: Version) -> bytes:
        if version >= Version.VER_88:
            return self.to_bytes_88(version)
        return self.to_bytes_84(version)
    def to_bytes_84(self, version: Version) -> bytes:
        research_location = -1
        research_time = 0
        button_id = 0
        hot_key = -1
        if len(self.research_locations):
            research_location = self.research_locations[0].location_id
            research_time = self.research_locations[0].research_time
            button_id = self.research_locations[0].button_id
            hot_key = self.research_locations[0].hot_key_id
        return b''.join([
            self.write_int_16_array(self.required_techs),
            self.write_class_array(self.resource_costs, version),
            self.write_int_16(self.required_tech_count),
            self.write_int_16(self.civ),
            self.write_int_16(self.full_tech_mode),
            self.write_int_16(research_location),
            self.write_int_32(self.language_dll_name),
            self.write_int_32(self.language_dll_description),
            self.write_int_16(research_time),
            self.write_int_16(self.effect_id),
            self.write_int_16(self.type),
            self.write_int_16(self.icon_id),
            self.write_int_8(button_id),
            self.write_int_32(self.language_dll_help),
            self.write_int_32(self.language_dll_tech_tree),
            self.write_int_32(hot_key),
            self.write_debug_string(self.name),
            self.write_int_8(self.repeatable),
        ])

    def to_bytes_88(self, version: Version) -> bytes:
        return b''.join([
            self.write_int_16_array(self.required_techs),
            self.write_class_array(self.resource_costs, version),
            self.write_int_16(self.required_tech_count),
            self.write_int_16(self.civ),
            self.write_int_16(self.full_tech_mode),
            self.write_int_32(self.language_dll_name),
            self.write_int_32(self.language_dll_description),
            self.write_int_16(self.effect_id),
            self.write_int_16(self.type),
            self.write_int_16(self.icon_id),
            self.write_int_32(self.language_dll_help),
            self.write_int_32(self.language_dll_tech_tree),
            self.write_debug_string(self.name),
            self.write_int_8(self.repeatable),
            self.write_int_16(len(self.research_locations)),
            self.write_class_array(self.research_locations, version),
        ])
