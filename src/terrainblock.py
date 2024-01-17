import typing
from dataclasses import dataclass

from src.common import ByteHandler, TILE_TYPE_COUNT, TERRAIN_COUNT, GenieClass
from src.terrain import Terrain
from src.tilesize import TileSize


@dataclass
class TerrainBlock(GenieClass):
    virtual_function_ptr: int
    map_pointer: int
    map_width: int
    map_height: int
    world_width: int
    world_height: int
    tile_sizes: list[TileSize]
    padding_ts: int
    terrains: list[Terrain]
    map_min_x: float
    map_min_y: float
    map_max_x: float
    map_max_y: float
    map_max_x_plus_1: float
    map_max_y_plus_1: float
    terrains_used_2: int
    borders_used: int
    max_terrain: int
    tile_width: int
    tile_height: int
    tile_half_height: int
    tile_half_width: int
    elev_height: int
    cur_row: int
    cur_col: int
    block_beg_row: int
    block_end_row: int
    block_beg_col: int
    block_end_col: int
    search_map_ptr: int
    search_map_rows_ptr: int
    any_frame_change: int
    map_visible_flag: int
    fog_flag: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'TerrainBlock':
        return cls(
            virtual_function_ptr=content.read_int_32(signed=False),
            map_pointer=content.read_int_32(signed=False),
            map_width=content.read_int_32(),
            map_height=content.read_int_32(),
            world_width=content.read_int_32(),
            world_height=content.read_int_32(),
            tile_sizes=content.read_class_array(TileSize, TILE_TYPE_COUNT),
            padding_ts=content.read_int_16(),
            terrains=content.read_class_array(Terrain, TERRAIN_COUNT),
            map_min_x=content.read_float(),
            map_min_y=content.read_float(),
            map_max_x=content.read_float(),
            map_max_y=content.read_float(),
            map_max_x_plus_1=content.read_float(),
            map_max_y_plus_1=content.read_float(),
            terrains_used_2=content.read_int_16(),
            borders_used=content.read_int_16(),
            max_terrain=content.read_int_16(),
            tile_width=content.read_int_16(),
            tile_height=content.read_int_16(),
            tile_half_height=content.read_int_16(),
            tile_half_width=content.read_int_16(),
            elev_height=content.read_int_16(),
            cur_row=content.read_int_16(),
            cur_col=content.read_int_16(),
            block_beg_row=content.read_int_16(),
            block_end_row=content.read_int_16(),
            block_beg_col=content.read_int_16(),
            block_end_col=content.read_int_16(),
            search_map_ptr=content.read_int_32(signed=False),
            search_map_rows_ptr=content.read_int_32(signed=False),
            any_frame_change=content.read_int_8(),
            map_visible_flag=content.read_int_8(),
            fog_flag=content.read_int_8(),
        )
