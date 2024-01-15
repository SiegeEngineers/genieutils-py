from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class MapTerrain(ByteHandler):
    proportion: int
    terrain: int
    clump_count: int
    edge_spacing: int
    placement_terrain: int
    clumpiness: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.proportion = self.read_int_32()
        self.terrain = self.read_int_32()
        self.clump_count = self.read_int_32()
        self.edge_spacing = self.read_int_32()
        self.placement_terrain = self.read_int_32()
        self.clumpiness = self.read_int_32()
