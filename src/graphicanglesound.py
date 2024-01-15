from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class GraphicAngleSound(ByteHandler):
    frame_num: int
    sound_id: int
    wwise_sound_id: int
    frame_num_2: int
    sound_id_2: int
    wwise_sound_id_2: int
    frame_num_3: int
    sound_id_3: int
    wwise_sound_id_3: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.frame_num = self.read_int_16()
        self.sound_id = self.read_int_16()
        self.wwise_sound_id = self.read_int_32()
        self.frame_num_2 = self.read_int_16()
        self.sound_id_2 = self.read_int_16()
        self.wwise_sound_id_2 = self.read_int_32()
        self.frame_num_3 = self.read_int_16()
        self.sound_id_3 = self.read_int_16()
        self.wwise_sound_id_3 = self.read_int_32()
