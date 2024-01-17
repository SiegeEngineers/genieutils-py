import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
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
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
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
