from dataclasses import dataclass

from src.common import ByteHandler
from src.sounditem import SoundItem


@dataclass
class Sound(ByteHandler):
    id: int
    play_delay: int
    items_size: int
    cache_time: int
    total_probability: int
    items: list[SoundItem]

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.id = self.read_int_16()
        self.play_delay = self.read_int_16()
        self.items_size = self.read_int_16()
        self.cache_time = self.read_int_32()
        self.total_probability = self.read_int_16()
        self.items = self.read_class_array(SoundItem, self.items_size)
