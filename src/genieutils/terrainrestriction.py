from dataclasses import dataclass

from genieutils.common import ByteHandler, GenieClass


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

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_32(self.exit_tile_sprite_id),
            self.write_int_32(self.enter_tile_sprite_id),
            self.write_int_32(self.walk_tile_sprite_id),
            self.write_int_32(self.walk_sprite_rate),
        ])


@dataclass
class TerrainRestriction(GenieClass):
    passable_buildable_dmg_multiplier: list[float]
    terrain_pass_graphics: list[TerrainPassGraphic]

    @classmethod
    def from_bytes_with_count(cls, content: ByteHandler, terrain_count: int) -> 'TerrainRestriction':
        return cls(
            passable_buildable_dmg_multiplier=content.read_float_array(terrain_count),
            terrain_pass_graphics=content.read_class_array(TerrainPassGraphic, terrain_count),
        )

    def to_bytes(self) -> bytes:
        assert len(self.passable_buildable_dmg_multiplier) == len(self.terrain_pass_graphics)
        return b''.join([
            self.write_float_array(self.passable_buildable_dmg_multiplier),
            self.write_class_array(self.terrain_pass_graphics),
        ])
