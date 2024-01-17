from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class MapUnit(GenieClass):
    unit: int
    host_terrain: int
    group_placing: int
    scale_flag: int
    padding_1: int
    objects_per_group: int
    fluctuation: int
    groups_per_player: int
    group_arena: int
    player_id: int
    set_place_for_all_players: int
    min_distance_to_players: int
    max_distance_to_players: int

    @classmethod
    def from_bytes(cls, content: ByteHandler):
        return cls(
            unit=content.read_int_32(),
            host_terrain=content.read_int_32(),
            group_placing=content.read_int_8(),
            scale_flag=content.read_int_8(),
            padding_1=content.read_int_16(),
            objects_per_group=content.read_int_32(),
            fluctuation=content.read_int_32(),
            groups_per_player=content.read_int_32(),
            group_arena=content.read_int_32(),
            player_id=content.read_int_32(),
            set_place_for_all_players=content.read_int_32(),
            min_distance_to_players=content.read_int_32(),
            max_distance_to_players=content.read_int_32(),
        )
