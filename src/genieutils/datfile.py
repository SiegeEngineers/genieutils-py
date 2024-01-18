import zlib
from dataclasses import dataclass
from os import PathLike
from pathlib import Path

from genieutils.civ import Civ
from genieutils.common import ByteHandler, GenieClass
from genieutils.effect import Effect
from genieutils.graphic import Graphic
from genieutils.playercolour import PlayerColour
from genieutils.randommaps import RandomMaps
from genieutils.sound import Sound
from genieutils.tech import Tech
from genieutils.techtree import TechTree
from genieutils.terrainblock import TerrainBlock
from genieutils.terrainrestriction import TerrainRestriction
from genieutils.unitheaders import UnitHeaders


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
    def parse(cls, input_file: Path | PathLike | str) -> 'DatFile':
        content = Path(input_file).read_bytes()
        data = zlib.decompress(content, wbits=-15)
        byte_handler = ByteHandler(memoryview(data))
        return cls.from_bytes(byte_handler)

    def save(self, target_file: Path | PathLike | str):
        uncompressed = self.to_bytes()
        compressed = zlib.compress(uncompressed, level=-1, wbits=-15)
        Path(target_file).write_bytes(compressed)

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'DatFile':
        version = content.read_string(8)
        terrain_restrictions_size = content.read_int_16()
        terrains_used_1 = content.read_int_16()
        float_ptr_terrain_tables = content.read_int_32_array(terrain_restrictions_size)
        terrain_pass_graphic_pointers = content.read_int_32_array(terrain_restrictions_size)
        terrain_restrictions = content.read_class_array_with_param(TerrainRestriction, terrain_restrictions_size,
                                                                   terrains_used_1)
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

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_string(8, self.version),
            self.write_int_16(self.terrain_restrictions_size),
            self.write_int_16(self.terrains_used_1),
            self.write_int_32_array(self.float_ptr_terrain_tables),
            self.write_int_32_array(self.terrain_pass_graphic_pointers),
            self.write_class_array(self.terrain_restrictions),
            self.write_int_16(self.player_colours_size),
            self.write_class_array(self.player_colours),
            self.write_int_16(self.sounds_size),
            self.write_class_array(self.sounds),
            self.write_int_16(self.graphics_size),
            self.write_int_32_array(self.graphic_pointers),
            self.write_class_array_with_pointers(self.graphic_pointers, self.graphics),
            self.write_class(self.terrain_block),
            self.write_class(self.random_maps),
            self.write_int_32(self.effects_size),
            self.write_class_array(self.effects),
            self.write_int_32(self.unit_headers_size),
            self.write_class_array(self.unit_headers),
            self.write_int_16(self.civs_size),
            self.write_class_array(self.civs),
            self.write_int_16(self.techs_size),
            self.write_class_array(self.techs),
            self.write_int_32(self.time_slice),
            self.write_int_32(self.unit_kill_rate),
            self.write_int_32(self.unit_kill_total),
            self.write_int_32(self.unit_hit_point_rate),
            self.write_int_32(self.unit_hit_point_total),
            self.write_int_32(self.razing_kill_rate),
            self.write_int_32(self.razing_kill_total),
            self.write_class(self.tech_tree),
        ])
