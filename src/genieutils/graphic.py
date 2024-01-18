from dataclasses import dataclass

from genieutils.common import ByteHandler, GenieClass


@dataclass
class GraphicDelta(GenieClass):
    graphic_id: int
    padding_1: int
    sprite_ptr: int
    offset_x: int
    offset_y: int
    display_angle: int
    padding_2: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'GraphicDelta':
        return cls(
            graphic_id=content.read_int_16(),
            padding_1=content.read_int_16(),
            sprite_ptr=content.read_int_32(),
            offset_x=content.read_int_16(),
            offset_y=content.read_int_16(),
            display_angle=content.read_int_16(),
            padding_2=content.read_int_16(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.graphic_id),
            self.write_int_16(self.padding_1),
            self.write_int_32(self.sprite_ptr),
            self.write_int_16(self.offset_x),
            self.write_int_16(self.offset_y),
            self.write_int_16(self.display_angle),
            self.write_int_16(self.padding_2),
        ])


@dataclass
class GraphicAngleSound(GenieClass):
    frame_num: int
    sound_id: int
    wwise_sound_id: int
    frame_num_2: int
    sound_id_2: int
    wwise_sound_id_2: int
    frame_num_3: int
    sound_id_3: int
    wwise_sound_id_3: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'GraphicAngleSound':
        return cls(
            frame_num=content.read_int_16(),
            sound_id=content.read_int_16(),
            wwise_sound_id=content.read_int_32(),
            frame_num_2=content.read_int_16(),
            sound_id_2=content.read_int_16(),
            wwise_sound_id_2=content.read_int_32(),
            frame_num_3=content.read_int_16(),
            sound_id_3=content.read_int_16(),
            wwise_sound_id_3=content.read_int_32(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.frame_num),
            self.write_int_16(self.sound_id),
            self.write_int_32(self.wwise_sound_id),
            self.write_int_16(self.frame_num_2),
            self.write_int_16(self.sound_id_2),
            self.write_int_32(self.wwise_sound_id_2),
            self.write_int_16(self.frame_num_3),
            self.write_int_16(self.sound_id_3),
            self.write_int_32(self.wwise_sound_id_3),
        ])


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

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_debug_string(self.name),
            self.write_debug_string(self.file_name),
            self.write_debug_string(self.particle_effect_name),
            self.write_int_32(self.slp),
            self.write_int_8(self.is_loaded),
            self.write_int_8(self.old_color_flag),
            self.write_int_8(self.layer),
            self.write_int_16(self.player_color),
            self.write_int_8(self.transparent_selection),
            self.write_int_16_array(self.coordinates),
            self.write_int_16(self.delta_count),
            self.write_int_16(self.sound_id),
            self.write_int_32(self.wwise_sound_id),
            self.write_int_8(self.angle_sounds_used),
            self.write_int_16(self.frame_count),
            self.write_int_16(self.angle_count),
            self.write_float(self.speed_multiplier),
            self.write_float(self.frame_duration),
            self.write_float(self.replay_delay),
            self.write_int_8(self.sequence_type),
            self.write_int_16(self.id),
            self.write_int_8(self.mirroring_mode),
            self.write_int_8(self.editor_flag),
            self.write_class_array(self.deltas),
            self.write_class_array(self.angle_sounds),
        ])
