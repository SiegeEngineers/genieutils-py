import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.terrainpassgraphic import TerrainPassGraphic


@dataclass
class TerrainRestriction(GenieClass):
    passable_buildable_dmg_multiplier: list[float]
    terrain_pass_graphics: list[TerrainPassGraphic]

    @classmethod
    def from_bytes_with_count(cls, content: ByteHandler, terrain_count: int) -> typing.Self:
        return cls(
            passable_buildable_dmg_multiplier=content.read_float_array(terrain_count),
            terrain_pass_graphics=content.read_class_array(TerrainPassGraphic, terrain_count),
        )
