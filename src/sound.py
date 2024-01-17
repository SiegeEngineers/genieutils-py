import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.sounditem import SoundItem


@dataclass
class Sound(GenieClass):
    id: int
    play_delay: int
    items_size: int
    cache_time: int
    total_probability: int
    items: list[SoundItem]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Sound':
        id_ = content.read_int_16()
        play_delay = content.read_int_16()
        items_size = content.read_int_16()
        cache_time = content.read_int_32()
        total_probability = content.read_int_16()
        items = content.read_class_array(SoundItem, items_size)
        return cls(
            id=id_,
            play_delay=play_delay,
            items_size=items_size,
            cache_time=cache_time,
            total_probability=total_probability,
            items=items,
        )
