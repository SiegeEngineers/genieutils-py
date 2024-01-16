from dataclasses import dataclass

from src.common import ByteHandler, TILE_TYPE_COUNT, TERRAIN_COUNT
from src.terrain import Terrain
from src.tilesize import TileSize


@dataclass
class TerrainBlock(ByteHandler):
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

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.virtual_function_ptr = self.read_int_32(signed=False)
        self.map_pointer = self.read_int_32(signed=False)
        self.map_width = self.read_int_32()
        self.map_height = self.read_int_32()
        self.world_width = self.read_int_32()
        self.world_height = self.read_int_32()
        self.tile_sizes = self.read_class_array(TileSize, TILE_TYPE_COUNT)
        self.padding_ts = self.read_int_16()
        self.terrains = self.read_class_array(Terrain, TERRAIN_COUNT)
        self.map_min_x = self.read_float()
        self.map_min_y = self.read_float()
        self.map_max_x = self.read_float()
        self.map_max_y = self.read_float()
        self.map_max_x_plus_1 = self.read_float()
        self.map_max_y_plus_1 = self.read_float()
        self.terrains_used_2 = self.read_int_16()
        self.borders_used = self.read_int_16()
        self.max_terrain = self.read_int_16()
        self.tile_width = self.read_int_16()
        self.tile_height = self.read_int_16()
        self.tile_half_height = self.read_int_16()
        self.tile_half_width = self.read_int_16()
        self.elev_height = self.read_int_16()
        self.cur_row = self.read_int_16()
        self.cur_col = self.read_int_16()
        self.block_beg_row = self.read_int_16()
        self.block_end_row = self.read_int_16()
        self.block_beg_col = self.read_int_16()
        self.block_end_col = self.read_int_16()
        self.search_map_ptr = self.read_int_32(signed=False)
        self.search_map_rows_ptr = self.read_int_32(signed=False)
        self.any_frame_change = self.read_int_8()
        self.map_visible_flag = self.read_int_8()
        self.fog_flag = self.read_int_8()
