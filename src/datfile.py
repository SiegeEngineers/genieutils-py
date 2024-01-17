import typing
import zlib
from dataclasses import dataclass
from pathlib import Path

from src.civ import Civ
from src.common import ByteHandler, GenieClass
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
class DatFile(GenieClass):
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

    @classmethod
    def parse(cls, input_file: Path) -> 'DatFile':
        content = input_file.read_bytes()
        data = zlib.decompress(content, wbits=-15)
        byte_handler = ByteHandler(memoryview(data))
        return cls.from_bytes(byte_handler)

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'DatFile':
        version = content.read_string(8)
        terrain_restrictions_size = content.read_int_16()
        terrains_used_1 = content.read_int_16()
        float_ptr_terrain_tables = content.read_int_32_array(terrain_restrictions_size)
        terrain_pass_graphic_pointers = content.read_int_32_array(terrain_restrictions_size)
        terrain_restrictions = content.read_class_array_with_param(TerrainRestriction, terrain_restrictions_size, terrains_used_1)
        player_colours_size = content.read_int_16()
        player_colours = content.read_class_array(PlayerColour, player_colours_size)
        sounds_size = content.read_int_16()
        sounds = content.read_class_array(Sound, sounds_size)
        graphics_size = content.read_int_16()
        graphic_pointers = content.read_int_32_array(graphics_size)
        graphics = content.read_class_array_with_pointers(Graphic, graphics_size, graphic_pointers)
        terrain_block = content.read_class(TerrainBlock)
        random_maps = content.read_class(RandomMaps)
        effects_size = content.read_int_32()
        effects = content.read_class_array(Effect, effects_size)
        unit_headers_size = content.read_int_32()
        unit_headers = content.read_class_array(UnitHeaders, unit_headers_size)
        civs_size = content.read_int_16()
        civs = content.read_class_array(Civ, civs_size)
        techs_size = content.read_int_16()
        techs = content.read_class_array(Tech, techs_size)
        time_slice = content.read_int_32()
        unit_kill_rate = content.read_int_32()
        unit_kill_total = content.read_int_32()
        unit_hit_point_rate = content.read_int_32()
        unit_hit_point_total = content.read_int_32()
        razing_kill_rate = content.read_int_32()
        razing_kill_total = content.read_int_32()
        tech_tree = content.read_class(TechTree)
        return cls(
            version,
            terrain_restrictions_size,
            terrains_used_1,
            float_ptr_terrain_tables,
            terrain_pass_graphic_pointers,
            terrain_restrictions,
            player_colours_size,
            player_colours,
            sounds_size,
            sounds,
            graphics_size,
            graphic_pointers,
            graphics,
            terrain_block,
            random_maps,
            effects_size,
            effects,
            unit_headers_size,
            unit_headers,
            civs_size,
            civs,
            techs_size,
            techs,
            time_slice,
            unit_kill_rate,
            unit_kill_total,
            unit_hit_point_rate,
            unit_hit_point_total,
            razing_kill_rate,
            razing_kill_total,
            tech_tree,
        )
