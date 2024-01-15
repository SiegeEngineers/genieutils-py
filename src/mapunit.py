from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class MapUnit(ByteHandler):
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

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.unit = self.read_int_32()
        self.host_terrain = self.read_int_32()
        self.group_placing = self.read_int_8()
        self.scale_flag = self.read_int_8()
        self.padding_1 = self.read_int_16()
        self.objects_per_group = self.read_int_32()
        self.fluctuation = self.read_int_32()
        self.groups_per_player = self.read_int_32()
        self.group_arena = self.read_int_32()
        self.player_id = self.read_int_32()
        self.set_place_for_all_players = self.read_int_32()
        self.min_distance_to_players = self.read_int_32()
        self.max_distance_to_players = self.read_int_32()
