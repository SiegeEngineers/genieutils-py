from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class TerrainPassGraphic(GenieClass):
    exit_tile_sprite_id: int
    enter_tile_sprite_id: int
    walk_tile_sprite_id: int
    walk_sprite_rate: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'TerrainPassGraphic':
        return cls(
            exit_tile_sprite_id=content.read_int_32(),
            enter_tile_sprite_id=content.read_int_32(),
            walk_tile_sprite_id=content.read_int_32(),
            walk_sprite_rate=content.read_int_32(),
        )
