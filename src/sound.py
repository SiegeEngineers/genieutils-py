from dataclasses import dataclass

from src.common import ByteHandler
from src.sounditem import SoundItem
from src.terrainpassgraphic import TerrainPassGraphic



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
        self.items = self.read_sound_items_array(self.items_size)

    def read_sound_items_array(self, size: int) -> list[SoundItem]:
        elements = []
        for i in range(size):
            sound_item = SoundItem(self.content[self.offset:])
            elements.append(sound_item)
            self.offset += sound_item.offset
        return elements
