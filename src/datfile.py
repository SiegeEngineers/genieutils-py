from dataclasses import dataclass

from src.civ import Civ
from src.common import ByteHandler
from src.effect import Effect
from src.graphic import Graphic
from src.playercolour import PlayerColour
from src.randommaps import RandomMaps
from src.sound import Sound
from src.tech import Tech
from src.techtree import TechTree
from src.terrainblock import TerrainBlock
from src.terrainrestriction import TerrainRestriction
from src.unitheaders import UnitHeaders


@dataclass
class DatFile(ByteHandler):
    version: str
    terrain_restrictions_size: int
    terrains_used_1: int
    float_ptr_terrain_tables: list[int]
    terrain_pass_graphic_pointers: list[int]
    terrain_restrictions: list[TerrainRestriction]
    player_colours_size: int
    player_colours: list[PlayerColour]
    sounds_size: int
    sounds: list[Sound]
    graphics_size: int
    graphic_pointers: list[int]
    graphics: list[Graphic | None]
    terrain_block: TerrainBlock
    random_maps: RandomMaps
    effects_size: int
    effects: list[Effect]
    unit_headers_size: int
    unit_headers: list[UnitHeaders]
    civs_size: int
    civs: list[Civ]
    techs_size: int
    techs: list[Tech]
    time_slice: int
    unit_kill_rate: int
    unit_kill_total: int
    unit_hit_point_rate: int
    unit_hit_point_total: int
    razing_kill_rate: int
    razing_kill_total: int
    tech_tree: TechTree

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.version = self.read_string(8)
        self.terrain_restrictions_size = self.read_int_16()
        self.terrains_used_1 = self.read_int_16()
        self.float_ptr_terrain_tables = self.read_int_32_array(self.terrain_restrictions_size)
        self.terrain_pass_graphic_pointers = self.read_int_32_array(self.terrain_restrictions_size)
        self.terrain_restrictions = self.read_terrain_restriction_array(self.terrain_restrictions_size)
        self.player_colours_size = self.read_int_16()
        self.player_colours = self.read_class_array(PlayerColour, self.player_colours_size)
        self.sounds_size = self.read_int_16()
        self.sounds = self.read_class_array(Sound, self.sounds_size)
        self.graphics_size = self.read_int_16()
        self.graphic_pointers = self.read_int_32_array(self.graphics_size)
        self.graphics = self.read_class_array_with_pointers(Graphic, self.graphics_size, self.graphic_pointers)
        self.terrain_block = self.read_class(TerrainBlock)
        self.random_maps = self.read_class(RandomMaps)
        self.effects_size = self.read_int_32()
        self.effects = self.read_class_array(Effect, self.effects_size)
        self.unit_headers_size = self.read_int_32()
        self.unit_headers = self.read_class_array(UnitHeaders, self.unit_headers_size)
        self.civs_size = self.read_int_16()
        self.civs = self.read_class_array(Civ, self.civs_size)
        self.techs_size = self.read_int_16()
        self.techs = self.read_class_array(Tech, self.techs_size)
        self.time_slice = self.read_int_32()
        self.unit_kill_rate = self.read_int_32()
        self.unit_kill_total = self.read_int_32()
        self.unit_hit_point_rate = self.read_int_32()
        self.unit_hit_point_total = self.read_int_32()
        self.razing_kill_rate = self.read_int_32()
        self.razing_kill_total = self.read_int_32()
        self.tech_tree = self.read_class(TechTree)

    def read_terrain_restriction_array(self, size: int) -> list[TerrainRestriction]:
        elements = []
        for i in range(size):
            terrain_restriction = TerrainRestriction(self.content[self.offset:], self.terrains_used_1)
            elements.append(terrain_restriction)
            self.offset += terrain_restriction.offset
        return elements
