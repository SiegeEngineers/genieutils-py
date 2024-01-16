from dataclasses import dataclass

from src.common import ByteHandler
from src.graphicanglesound import GraphicAngleSound
from src.graphicdelta import GraphicDelta


@dataclass
class Graphic(ByteHandler):
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

    def __init__(self, content: memoryview, pointers: list[int]):
        super().__init__(content)

        self.name = self.read_debug_string()
        self.file_name = self.read_debug_string()
        self.particle_effect_name = self.read_debug_string()
        self.slp = self.read_int_32()
        self.is_loaded = self.read_int_8()
        self.old_color_flag = self.read_int_8()
        self.layer = self.read_int_8()
        self.player_color = self.read_int_16()
        self.transparent_selection = self.read_int_8()
        self.coordinates = self.read_int_16_array(4)
        self.delta_count = self.read_int_16()
        self.sound_id = self.read_int_16()
        self.wwise_sound_id = self.read_int_32()
        self.angle_sounds_used = self.read_int_8()
        self.frame_count = self.read_int_16()
        self.angle_count = self.read_int_16()
        self.speed_multiplier = self.read_float()
        self.frame_duration = self.read_float()
        self.replay_delay = self.read_float()
        self.sequence_type = self.read_int_8()
        self.id = self.read_int_16()
        self.mirroring_mode = self.read_int_8()
        self.editor_flag = self.read_int_8()
        self.deltas = self.read_graphic_deltas_array(self.delta_count)
        self.angle_sounds = self.read_angle_sounds_array(self.angle_sounds_used, self.angle_count)

    def read_graphic_deltas_array(self, size: int) -> list[GraphicDelta]:
        elements = []
        for i in range(size):
            graphic_delta = GraphicDelta(self.content[self.offset:])
            elements.append(graphic_delta)
            self.offset += graphic_delta.offset
        return elements

    def read_angle_sounds_array(self, used: int, size: int) -> list[GraphicAngleSound]:
        elements = []
        if used:
            for i in range(size):
                graphic_delta = GraphicAngleSound(self.content[self.offset:])
                elements.append(graphic_delta)
                self.offset += graphic_delta.offset
        return elements
