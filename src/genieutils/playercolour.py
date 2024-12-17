from dataclasses import dataclass

from genieutils.common import ByteHandler, GenieClass
from genieutils.versions import Version


@dataclass(slots=True)
class PlayerColour(GenieClass):
    id: int
    player_color_base: int
    unit_outline_color: int
    unit_selection_color_1: int
    unit_selection_color_2: int
    minimap_color: int
    minimap_color_2: int
    minimap_color_3: int
    statistics_text: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'PlayerColour':
        return cls(
            id=content.read_int_32(),
            player_color_base=content.read_int_32(),
            unit_outline_color=content.read_int_32(),
            unit_selection_color_1=content.read_int_32(),
            unit_selection_color_2=content.read_int_32(),
            minimap_color=content.read_int_32(),
            minimap_color_2=content.read_int_32(),
            minimap_color_3=content.read_int_32(),
            statistics_text=content.read_int_32(),
        )

    def to_bytes(self, version: Version) -> bytes:
        return b''.join([
            self.write_int_32(self.id),
            self.write_int_32(self.player_color_base),
            self.write_int_32(self.unit_outline_color),
            self.write_int_32(self.unit_selection_color_1),
            self.write_int_32(self.unit_selection_color_2),
            self.write_int_32(self.minimap_color),
            self.write_int_32(self.minimap_color_2),
            self.write_int_32(self.minimap_color_3),
            self.write_int_32(self.statistics_text),
        ])
