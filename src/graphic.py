import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.graphicanglesound import GraphicAngleSound
from src.graphicdelta import GraphicDelta


@dataclass
class Graphic(GenieClass):
    name: str
    file_name: str
    particle_effect_name: str
    slp: int
    is_loaded: int
    old_color_flag: int
    layer: int
    player_color: int
    transparent_selection: int
    coordinates: list[int]
    delta_count: int
    sound_id: int
    wwise_sound_id: int
    angle_sounds_used: int
    frame_count: int
    angle_count: int
    speed_multiplier: float
    frame_duration: float
    replay_delay: float
    sequence_type: int
    id: int
    mirroring_mode: int
    editor_flag: int
    deltas: list[GraphicDelta]
    angle_sounds: list[GraphicAngleSound]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Graphic':
        name = content.read_debug_string()
        file_name = content.read_debug_string()
        particle_effect_name = content.read_debug_string()
        slp = content.read_int_32()
        is_loaded = content.read_int_8()
        old_color_flag = content.read_int_8()
        layer = content.read_int_8()
        player_color = content.read_int_16()
        transparent_selection = content.read_int_8()
        coordinates = content.read_int_16_array(4)
        delta_count = content.read_int_16()
        sound_id = content.read_int_16()
        wwise_sound_id = content.read_int_32()
        angle_sounds_used = content.read_int_8()
        frame_count = content.read_int_16()
        angle_count = content.read_int_16()
        speed_multiplier = content.read_float()
        frame_duration = content.read_float()
        replay_delay = content.read_float()
        sequence_type = content.read_int_8()
        id_ = content.read_int_16()
        mirroring_mode = content.read_int_8()
        editor_flag = content.read_int_8()
        deltas = content.read_class_array(GraphicDelta, delta_count)
        angle_sounds = content.read_class_array(GraphicAngleSound, angle_count) if angle_sounds_used else []
        return cls(
            name=name,
            file_name=file_name,
            particle_effect_name=particle_effect_name,
            slp=slp,
            is_loaded=is_loaded,
            old_color_flag=old_color_flag,
            layer=layer,
            player_color=player_color,
            transparent_selection=transparent_selection,
            coordinates=coordinates,
            delta_count=delta_count,
            sound_id=sound_id,
            wwise_sound_id=wwise_sound_id,
            angle_sounds_used=angle_sounds_used,
            frame_count=frame_count,
            angle_count=angle_count,
            speed_multiplier=speed_multiplier,
            frame_duration=frame_duration,
            replay_delay=replay_delay,
            sequence_type=sequence_type,
            id=id_,
            mirroring_mode=mirroring_mode,
            editor_flag=editor_flag,
            deltas=deltas,
            angle_sounds=angle_sounds,
        )
