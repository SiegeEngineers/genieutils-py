from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class MapElevation(ByteHandler):
    proportion: int
    terrain: int
    clump_count: int
    base_terrain: int
    base_elevation: int
    tile_spacing: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.proportion = self.read_int_32()
        self.terrain = self.read_int_32()
        self.clump_count = self.read_int_32()
        self.base_terrain = self.read_int_32()
        self.base_elevation = self.read_int_32()
        self.tile_spacing = self.read_int_32()
