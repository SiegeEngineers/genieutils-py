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
        self.terrain_pass_graphics = self.read_terrain_pass_graphic_array(terrain_count)

    def read_terrain_pass_graphic_array(self, size: int) -> list[TerrainPassGraphic]:
        elements = []
        for i in range(size):
            terrain_pass_graphic = TerrainPassGraphic(self.content[self.offset:])
            elements.append(terrain_pass_graphic)
            self.offset += terrain_pass_graphic.offset
        return elements
