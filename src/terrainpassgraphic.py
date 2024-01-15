from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class TerrainPassGraphic(ByteHandler):
    exit_tile_sprite_id: int
    enter_tile_sprite_id: int
    walk_tile_sprite_id: int
    walk_sprite_rate: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.exit_tile_sprite_id = self.read_int_32()
        self.enter_tile_sprite_id = self.read_int_32()
        self.walk_tile_sprite_id = self.read_int_32()
        self.walk_sprite_rate = self.read_int_32()

