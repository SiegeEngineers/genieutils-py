import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


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
