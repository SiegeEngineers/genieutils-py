from dataclasses import dataclass

from src.common import ByteHandler, TILE_TYPE_COUNT, TERRAIN_UNITS_SIZE
from src.framedata import FrameData


@dataclass
class Terrain(ByteHandler):
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
    cliffColors: list[int]
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

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.enabled = self.read_int_8()
        self.random = self.read_int_8()
        self.is_water = self.read_int_8()
        self.hide_in_editor = self.read_int_8()
        self.string_id = self.read_int_32()
        self.name = self.read_debug_string()
        self.name_2 = self.read_debug_string()
        self.slp = self.read_int_32()
        self.shape_ptr = self.read_int_32()
        self.sound_id = self.read_int_32()
        self.wwise_sound_id = self.read_int_32(signed=False)
        self.wwise_sound_stop_id = self.read_int_32(signed=False)
        self.blend_priority = self.read_int_32()
        self.blend_type = self.read_int_32()
        self.overlay_mask_name = self.read_debug_string()
        self.colors = self.read_int_8_array(3)
        self.cliffColors = self.read_int_8_array(2)
        self.passable_terrain = self.read_int_8()
        self.impassable_terrain = self.read_int_8()
        self.is_animated = self.read_int_8()
        self.animation_frames = self.read_int_16()
        self.pause_frames = self.read_int_16()
        self.interval = self.read_float()
        self.pause_between_loops = self.read_float()
        self.frame = self.read_int_16()
        self.draw_frame = self.read_int_16()
        self.animate_last = self.read_float()
        self.frame_changed = self.read_int_8()
        self.drawn = self.read_int_8()
        self.frame_data = self.read_class_array(FrameData, TILE_TYPE_COUNT)
        self.terrain_to_draw = self.read_int_16()
        self.terrain_dimensions = self.read_int_16_array(2)
        self.terrain_unit_masked_density = self.read_int_16_array(TERRAIN_UNITS_SIZE)
        self.terrain_unit_id = self.read_int_16_array(TERRAIN_UNITS_SIZE)
        self.terrain_unit_density = self.read_int_16_array(TERRAIN_UNITS_SIZE)
        self.terrain_unit_centering = self.read_int_8_array(TERRAIN_UNITS_SIZE)
        self.number_of_terrain_units_used = self.read_int_16()
        self.phantom = self.read_int_16()
