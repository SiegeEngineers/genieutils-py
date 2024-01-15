from dataclasses import dataclass

from src.common import ByteHandler
from src.effect import Effect
from src.graphic import Graphic
from src.playercolour import PlayerColour
from src.randommaps import RandomMaps
from src.sound import Sound
from src.terrainblock import TerrainBlock
from src.terrainrestriction import TerrainRestriction


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
    # unit_headers_size: int
    # unit_headers: list[UnitHeader]
    # civs_size: int
    # civs: list[Civ]
    # techs_size: int
    # techs: list[Tech]
    # time_slice: int
    # unit_kill_rate: int
    # unit_kill_total: int
    # unit_hit_point_rate: int
    # unit_hit_point_total: int
    # razing_kill_rate: int
    # razing_kill_total: int
    # tech_tree: TechTree

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.version = self.read_string(8)
        self.terrain_restrictions_size = self.read_int_16()
        self.terrains_used_1 = self.read_int_16()
        self.float_ptr_terrain_tables = self.read_int_32_array(self.terrain_restrictions_size)
        self.terrain_pass_graphic_pointers = self.read_int_32_array(self.terrain_restrictions_size)
        self.terrain_restrictions = self.read_terrain_restriction_array(self.terrain_restrictions_size)
        self.player_colours_size = self.read_int_16()
        self.player_colours = self.read_player_colours_array(self.player_colours_size)
        self.sounds_size = self.read_int_16()
        self.sounds = self.read_sounds_array(self.sounds_size)
        self.graphics_size = self.read_int_16()
        self.graphic_pointers = self.read_int_32_array(self.graphics_size)
        self.graphics = self.read_graphics_array(self.graphics_size, self.graphic_pointers)
        self.terrain_block = self.read_terrain_block()
        self.random_maps = self.read_random_maps()
        self.effects_size = self.read_int_32()
        self.effects = self.read_effects_array(self.effects_size)
        # self.unit_headers_size = self.read_int_32()
        # self.unit_headers = self.read_unit_headers_array(self.unit_headers_size)
        # self.civs_size = self.read_int_16()
        # self.civs = self.read_civ_array(self.civs_size)
        # self.techs_size = self.read_int_16()
        # self.techs = self.read_tech_array(self.techs_size)
        # self.time_slice = self.read_int_32()
        # self.unit_kill_rate = self.read_int_32()
        # self.unit_kill_total = self.read_int_32()
        # self.unit_hit_point_rate = self.read_int_32()
        # self.unit_hit_point_total = self.read_int_32()
        # self.razing_kill_rate = self.read_int_32()
        # self.razing_kill_total = self.read_int_32()
        # self.tech_tree = self.read_tech_tree()

    def read_terrain_restriction_array(self, size: int) -> list[TerrainRestriction]:
        elements = []
        for i in range(size):
            terrain_restriction = TerrainRestriction(self.content[self.offset:], self.terrains_used_1)
            elements.append(terrain_restriction)
            self.offset += terrain_restriction.offset
        return elements

    def read_player_colours_array(self, size: int) -> list[PlayerColour]:
        elements = []
        for i in range(size):
            player_colour = PlayerColour(self.content[self.offset:])
            elements.append(player_colour)
            self.offset += player_colour.offset
        return elements

    def read_sounds_array(self, size: int) -> list[Sound]:
        elements = []
        for i in range(size):
            sound = Sound(self.content[self.offset:])
            elements.append(sound)
            self.offset += sound.offset
        return elements

    def read_graphics_array(self, size: int, pointers: list[int]) -> list[Graphic | None]:
        elements = []
        for i in range(size):
            graphic = None
            if pointers[i]:
                graphic = Graphic(self.content[self.offset:], pointers)
                self.offset += graphic.offset
            elements.append(graphic)
        return elements

    def read_terrain_block(self) -> TerrainBlock:
        terrain_block = TerrainBlock(self.content[self.offset:])
        self.offset += terrain_block.offset
        return terrain_block

    def read_random_maps(self) -> RandomMaps:
        random_maps = RandomMaps(self.content[self.offset:])
        self.offset += random_maps.offset
        return random_maps

    def read_effects_array(self, size: int) -> list[Effect]:
        elements = []
        for i in range(size):
            effect = Effect(self.content[self.offset:])
            elements.append(effect)
            self.offset += effect.offset
        return elements

    # def read_unit_headers_array(self, size: int) -> list[UnitHeaders]:
    #     elements = []
    #     for i in range(size):
    #         unit_headers = UnitHeaders(self.content[self.offset:])
    #         elements.append(unit_headers)
    #         self.offset += unit_headers.offset
    #     return elements
    #
    # def read_civ_array(self, size: int) -> list[Civ]:
    #     elements = []
    #     for i in range(size):
    #         civ = Civ(self.content[self.offset:])
    #         elements.append(civ)
    #         self.offset += civ.offset
    #     return elements
    #
    # def read_tech_array(self, size: int) -> list[Tech]:
    #     elements = []
    #     for i in range(size):
    #         tech = Tech(self.content[self.offset:])
    #         elements.append(tech)
    #         self.offset += tech.offset
    #     return elements
    #
    # def read_tech_tree(self) -> TechTree:
    #     random_maps = TechTree(self.content[self.offset:])
    #     self.offset += random_maps.offset
    #     return random_maps
