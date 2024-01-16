from dataclasses import dataclass

from src.common import ByteHandler
from src.terrainpassgraphic import TerrainPassGraphic


@dataclass
class TerrainRestriction(ByteHandler):
    passable_buildable_dmg_multiplier: list[float]
    terrain_pass_graphics: list[TerrainPassGraphic]

    def __init__(self, content: memoryview, terrain_count: int):
        super().__init__(content)
        self.passable_buildable_dmg_multiplier = self.read_float_array(terrain_count)
        self.terrain_pass_graphics = self.read_class_array(TerrainPassGraphic, terrain_count)
