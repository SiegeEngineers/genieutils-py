from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class MapLand(ByteHandler):
    land_id: int
    terrain: int
    land_spacing: int
    base_size: int
    zone: int
    placement_type: int
    padding_1: int
    base_x: int
    base_y: int
    land_proportion: int
    by_player_flag: int
    padding_2: int
    start_area_radius: int
    terrain_edge_fade: int
    clumpiness: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.land_id = self.read_int_32()
        self.terrain = self.read_int_32(signed=False)
        self.land_spacing = self.read_int_32()
        self.base_size = self.read_int_32()
        self.zone = self.read_int_8()
        self.placement_type = self.read_int_8()
        self.padding_1 = self.read_int_16()
        self.base_x = self.read_int_32()
        self.base_y = self.read_int_32()
        self.land_proportion = self.read_int_8()
        self.by_player_flag = self.read_int_8()
        self.padding_2 = self.read_int_16()
        self.start_area_radius = self.read_int_32()
        self.terrain_edge_fade = self.read_int_32()
        self.clumpiness = self.read_int_32()
