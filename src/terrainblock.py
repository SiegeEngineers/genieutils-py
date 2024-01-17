from dataclasses import dataclass

from src.common import ByteHandler, TILE_TYPE_COUNT, TERRAIN_COUNT, GenieClass, TERRAIN_UNITS_SIZE


@dataclass
class FrameData(GenieClass):
    frame_count: int
    angle_count: int
    shape_id: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'FrameData':
        return cls(
            frame_count=content.read_int_16(),
            angle_count=content.read_int_16(),
            shape_id=content.read_int_16(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.frame_count),
            self.write_int_16(self.angle_count),
            self.write_int_16(self.shape_id),
        ])


@dataclass
class Terrain(GenieClass):
    enabled: int
    random: int
    is_water: int
    hide_in_editor: int
    string_id: int
    name: str
    name_2: str
    slp: int
    shape_ptr: int
    sound_id: int
    wwise_sound_id: int
    wwise_sound_stop_id: int
    blend_priority: int
    blend_type: int
    overlay_mask_name: str
    colors: list[int]
    cliff_colors: list[int]
    passable_terrain: int
    impassable_terrain: int
    is_animated: int
    animation_frames: int
    pause_frames: int
    interval: float
    pause_between_loops: float
    frame: int
    draw_frame: int
    animate_last: float
    frame_changed: int
    drawn: int
    frame_data: list[FrameData]
    terrain_to_draw: int
    terrain_dimensions: list[int]
    terrain_unit_masked_density: list[int]
    terrain_unit_id: list[int]
    terrain_unit_density: list[int]
    terrain_unit_centering: list[int]
    number_of_terrain_units_used: int
    phantom: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Terrain':
        return cls(
            enabled=content.read_int_8(),
            random=content.read_int_8(),
            is_water=content.read_int_8(),
            hide_in_editor=content.read_int_8(),
            string_id=content.read_int_32(),
            name=content.read_debug_string(),
            name_2=content.read_debug_string(),
            slp=content.read_int_32(),
            shape_ptr=content.read_int_32(),
            sound_id=content.read_int_32(),
            wwise_sound_id=content.read_int_32(signed=False),
            wwise_sound_stop_id=content.read_int_32(signed=False),
            blend_priority=content.read_int_32(),
            blend_type=content.read_int_32(),
            overlay_mask_name=content.read_debug_string(),
            colors=content.read_int_8_array(3),
            cliff_colors=content.read_int_8_array(2),
            passable_terrain=content.read_int_8(),
            impassable_terrain=content.read_int_8(),
            is_animated=content.read_int_8(),
            animation_frames=content.read_int_16(),
            pause_frames=content.read_int_16(),
            interval=content.read_float(),
            pause_between_loops=content.read_float(),
            frame=content.read_int_16(),
            draw_frame=content.read_int_16(),
            animate_last=content.read_float(),
            frame_changed=content.read_int_8(),
            drawn=content.read_int_8(),
            frame_data=content.read_class_array(FrameData, TILE_TYPE_COUNT),
            terrain_to_draw=content.read_int_16(),
            terrain_dimensions=content.read_int_16_array(2),
            terrain_unit_masked_density=content.read_int_16_array(TERRAIN_UNITS_SIZE),
            terrain_unit_id=content.read_int_16_array(TERRAIN_UNITS_SIZE),
            terrain_unit_density=content.read_int_16_array(TERRAIN_UNITS_SIZE),
            terrain_unit_centering=content.read_int_8_array(TERRAIN_UNITS_SIZE),
            number_of_terrain_units_used=content.read_int_16(),
            phantom=content.read_int_16(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_8(self.enabled),
            self.write_int_8(self.random),
            self.write_int_8(self.is_water),
            self.write_int_8(self.hide_in_editor),
            self.write_int_32(self.string_id),
            self.write_debug_string(self.name),
            self.write_debug_string(self.name_2),
            self.write_int_32(self.slp),
            self.write_int_32(self.shape_ptr),
            self.write_int_32(self.sound_id),
            self.write_int_32(self.wwise_sound_id, signed=False),
            self.write_int_32(self.wwise_sound_stop_id, signed=False),
            self.write_int_32(self.blend_priority),
            self.write_int_32(self.blend_type),
            self.write_debug_string(self.overlay_mask_name),
            self.write_int_8_array(self.colors),
            self.write_int_8_array(self.cliff_colors),
            self.write_int_8(self.passable_terrain),
            self.write_int_8(self.impassable_terrain),
            self.write_int_8(self.is_animated),
            self.write_int_16(self.animation_frames),
            self.write_int_16(self.pause_frames),
            self.write_float(self.interval),
            self.write_float(self.pause_between_loops),
            self.write_int_16(self.frame),
            self.write_int_16(self.draw_frame),
            self.write_float(self.animate_last),
            self.write_int_8(self.frame_changed),
            self.write_int_8(self.drawn),
            self.write_class_array(self.frame_data),
            self.write_int_16(self.terrain_to_draw),
            self.write_int_16_array(self.terrain_dimensions),
            self.write_int_16_array(self.terrain_unit_masked_density),
            self.write_int_16_array(self.terrain_unit_id),
            self.write_int_16_array(self.terrain_unit_density),
            self.write_int_8_array(self.terrain_unit_centering),
            self.write_int_16(self.number_of_terrain_units_used),
            self.write_int_16(self.phantom),
        ])


@dataclass
class TileSize(GenieClass):
    width: int
    height: int
    delta_y: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'TileSize':
        return cls(
            width=content.read_int_16(),
            height=content.read_int_16(),
            delta_y=content.read_int_16(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.width),
            self.write_int_16(self.height),
            self.write_int_16(self.delta_y),
        ])


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

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_32(self.virtual_function_ptr, signed=False),
            self.write_int_32(self.map_pointer, signed=False),
            self.write_int_32(self.map_width),
            self.write_int_32(self.map_height),
            self.write_int_32(self.world_width),
            self.write_int_32(self.world_height),
            self.write_class_array(self.tile_sizes),
            self.write_int_16(self.padding_ts),
            self.write_class_array(self.terrains),
            self.write_float(self.map_min_x),
            self.write_float(self.map_min_y),
            self.write_float(self.map_max_x),
            self.write_float(self.map_max_y),
            self.write_float(self.map_max_x_plus_1),
            self.write_float(self.map_max_y_plus_1),
            self.write_int_16(self.terrains_used_2),
            self.write_int_16(self.borders_used),
            self.write_int_16(self.max_terrain),
            self.write_int_16(self.tile_width),
            self.write_int_16(self.tile_height),
            self.write_int_16(self.tile_half_height),
            self.write_int_16(self.tile_half_width),
            self.write_int_16(self.elev_height),
            self.write_int_16(self.cur_row),
            self.write_int_16(self.cur_col),
            self.write_int_16(self.block_beg_row),
            self.write_int_16(self.block_end_row),
            self.write_int_16(self.block_beg_col),
            self.write_int_16(self.block_end_col),
            self.write_int_32(self.search_map_ptr, signed=False),
            self.write_int_32(self.search_map_rows_ptr, signed=False),
            self.write_int_8(self.any_frame_change),
            self.write_int_8(self.map_visible_flag),
            self.write_int_8(self.fog_flag),
        ])
