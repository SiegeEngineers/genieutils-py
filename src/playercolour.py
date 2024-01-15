from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class PlayerColour(ByteHandler):
    id: int
    player_color_base: int
    unit_outline_color: int
    unit_selection_color_1: int
    unit_selection_color_2: int
    minimap_color: int
    minimap_color_2: int
    minimap_color_3: int
    statistics_text: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.id = self.read_int_32()
        self.player_color_base = self.read_int_32()
        self.unit_outline_color = self.read_int_32()
        self.unit_selection_color_1 = self.read_int_32()
        self.unit_selection_color_2 = self.read_int_32()
        self.minimap_color = self.read_int_32()
        self.minimap_color_2 = self.read_int_32()
        self.minimap_color_3 = self.read_int_32()
        self.statistics_text = self.read_int_32()
