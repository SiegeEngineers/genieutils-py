import typing
from dataclasses import dataclass

from src.common import ByteHandler, TILE_TYPE_COUNT, TERRAIN_UNITS_SIZE, GenieClass
from src.framedata import FrameData


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

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
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
            cliffColors=content.read_int_8_array(2),
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
