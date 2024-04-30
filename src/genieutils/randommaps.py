from dataclasses import dataclass

from genieutils.common import ByteHandler, GenieClass
from genieutils.versions import Version


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
    def from_bytes(cls, content: ByteHandler) -> 'MapUnit':
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

    def to_bytes(self, version: Version) -> bytes:
        return b''.join([
            self.write_int_32(self.unit),
            self.write_int_32(self.host_terrain),
            self.write_int_8(self.group_placing),
            self.write_int_8(self.scale_flag),
            self.write_int_16(self.padding_1),
            self.write_int_32(self.objects_per_group),
            self.write_int_32(self.fluctuation),
            self.write_int_32(self.groups_per_player),
            self.write_int_32(self.group_arena),
            self.write_int_32(self.player_id),
            self.write_int_32(self.set_place_for_all_players),
            self.write_int_32(self.min_distance_to_players),
            self.write_int_32(self.max_distance_to_players),
        ])


@dataclass
class MapTerrain(GenieClass):
    proportion: int
    terrain: int
    clump_count: int
    edge_spacing: int
    placement_terrain: int
    clumpiness: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'MapTerrain':
        return cls(
            proportion=content.read_int_32(),
            terrain=content.read_int_32(),
            clump_count=content.read_int_32(),
            edge_spacing=content.read_int_32(),
            placement_terrain=content.read_int_32(),
            clumpiness=content.read_int_32(),
        )

    def to_bytes(self, version: Version) -> bytes:
        return b''.join([
            self.write_int_32(self.proportion),
            self.write_int_32(self.terrain),
            self.write_int_32(self.clump_count),
            self.write_int_32(self.edge_spacing),
            self.write_int_32(self.placement_terrain),
            self.write_int_32(self.clumpiness),
        ])


@dataclass
class MapLand(GenieClass):
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

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'MapLand':
        return cls(
            land_id=content.read_int_32(),
            terrain=content.read_int_32(signed=False),
            land_spacing=content.read_int_32(),
            base_size=content.read_int_32(),
            zone=content.read_int_8(),
            placement_type=content.read_int_8(),
            padding_1=content.read_int_16(),
            base_x=content.read_int_32(),
            base_y=content.read_int_32(),
            land_proportion=content.read_int_8(),
            by_player_flag=content.read_int_8(),
            padding_2=content.read_int_16(),
            start_area_radius=content.read_int_32(),
            terrain_edge_fade=content.read_int_32(),
            clumpiness=content.read_int_32(),
        )

    def to_bytes(self, version: Version) -> bytes:
        return b''.join([
            self.write_int_32(self.land_id),
            self.write_int_32(self.terrain, signed=False),
            self.write_int_32(self.land_spacing),
            self.write_int_32(self.base_size),
            self.write_int_8(self.zone),
            self.write_int_8(self.placement_type),
            self.write_int_16(self.padding_1),
            self.write_int_32(self.base_x),
            self.write_int_32(self.base_y),
            self.write_int_8(self.land_proportion),
            self.write_int_8(self.by_player_flag),
            self.write_int_16(self.padding_2),
            self.write_int_32(self.start_area_radius),
            self.write_int_32(self.terrain_edge_fade),
            self.write_int_32(self.clumpiness),
        ])


@dataclass
class MapElevation(GenieClass):
    proportion: int
    terrain: int
    clump_count: int
    base_terrain: int
    base_elevation: int
    tile_spacing: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'MapElevation':
        return cls(
            proportion=content.read_int_32(),
            terrain=content.read_int_32(),
            clump_count=content.read_int_32(),
            base_terrain=content.read_int_32(),
            base_elevation=content.read_int_32(),
            tile_spacing=content.read_int_32(),
        )

    def to_bytes(self, version: Version) -> bytes:
        return b''.join([
            self.write_int_32(self.proportion),
            self.write_int_32(self.terrain),
            self.write_int_32(self.clump_count),
            self.write_int_32(self.base_terrain),
            self.write_int_32(self.base_elevation),
            self.write_int_32(self.tile_spacing),
        ])


@dataclass
class MapInfo(GenieClass):
    map_id: int
    border_south_west: int
    border_north_west: int
    border_north_east: int
    border_south_east: int
    border_usage: int
    water_shape: int
    base_terrain: int
    land_coverage: int
    unused_id: int
    map_lands_size: int
    map_lands_ptr: int
    map_lands: list[MapLand]
    map_terrains_size: int
    map_terrains_ptr: int
    map_terrains: list[MapTerrain]
    map_units_size: int
    map_units_ptr: int
    map_units: list[MapUnit]
    map_elevations_size: int
    map_elevations_ptr: int
    map_elevations: list[MapElevation]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'MapInfo':
        map_id = content.read_int_32()
        border_south_west = content.read_int_32()
        border_north_west = content.read_int_32()
        border_north_east = content.read_int_32()
        border_south_east = content.read_int_32()
        border_usage = content.read_int_32()
        water_shape = content.read_int_32()
        base_terrain = content.read_int_32()
        land_coverage = content.read_int_32()
        unused_id = content.read_int_32()
        map_lands_size = content.read_int_32(signed=False)
        map_lands_ptr = content.read_int_32()
        map_lands = content.read_class_array(MapLand, map_lands_size)
        map_terrains_size = content.read_int_32(signed=False)
        map_terrains_ptr = content.read_int_32()
        map_terrains = content.read_class_array(MapTerrain, map_terrains_size)
        map_units_size = content.read_int_32(signed=False)
        map_units_ptr = content.read_int_32()
        map_units = content.read_class_array(MapUnit, map_units_size)
        map_elevations_size = content.read_int_32(signed=False)
        map_elevations_ptr = content.read_int_32()
        map_elevations = content.read_class_array(MapElevation, map_elevations_size)
        return cls(
            map_id=map_id,
            border_south_west=border_south_west,
            border_north_west=border_north_west,
            border_north_east=border_north_east,
            border_south_east=border_south_east,
            border_usage=border_usage,
            water_shape=water_shape,
            base_terrain=base_terrain,
            land_coverage=land_coverage,
            unused_id=unused_id,
            map_lands_size=map_lands_size,
            map_lands_ptr=map_lands_ptr,
            map_lands=map_lands,
            map_terrains_size=map_terrains_size,
            map_terrains_ptr=map_terrains_ptr,
            map_terrains=map_terrains,
            map_units_size=map_units_size,
            map_units_ptr=map_units_ptr,
            map_units=map_units,
            map_elevations_size=map_elevations_size,
            map_elevations_ptr=map_elevations_ptr,
            map_elevations=map_elevations,
        )

    def to_bytes(self, version: Version) -> bytes:
        return b''.join([
            self.write_int_32(self.map_id),
            self.write_int_32(self.border_south_west),
            self.write_int_32(self.border_north_west),
            self.write_int_32(self.border_north_east),
            self.write_int_32(self.border_south_east),
            self.write_int_32(self.border_usage),
            self.write_int_32(self.water_shape),
            self.write_int_32(self.base_terrain),
            self.write_int_32(self.land_coverage),
            self.write_int_32(self.unused_id),
            self.write_int_32(self.map_lands_size, signed=False),
            self.write_int_32(self.map_lands_ptr),
            self.write_class_array(self.map_lands, version),
            self.write_int_32(self.map_terrains_size, signed=False),
            self.write_int_32(self.map_terrains_ptr),
            self.write_class_array(self.map_terrains, version),
            self.write_int_32(self.map_units_size, signed=False),
            self.write_int_32(self.map_units_ptr),
            self.write_class_array(self.map_units, version),
            self.write_int_32(self.map_elevations_size, signed=False),
            self.write_int_32(self.map_elevations_ptr),
            self.write_class_array(self.map_elevations, version),
        ])


@dataclass
class RandomMaps(GenieClass):
    random_maps_ptr: int
    map_info_1: list[MapInfo]
    map_info_2: list[MapInfo]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'RandomMaps':
        random_map_count = content.read_int_32(signed=False)
        random_maps_ptr = content.read_int_32()
        map_info_1 = content.read_class_array(MapInfo, random_map_count)
        map_info_2 = content.read_class_array(MapInfo, random_map_count)
        return cls(
            random_maps_ptr=random_maps_ptr,
            map_info_1=map_info_1,
            map_info_2=map_info_2,
        )

    def to_bytes(self, version: Version) -> bytes:
        assert len(self.map_info_1) == len(self.map_info_2)
        return b''.join([
            self.write_int_32(len(self.map_info_1), signed=False),
            self.write_int_32(self.random_maps_ptr),
            self.write_class_array(self.map_info_1, version),
            self.write_class_array(self.map_info_2, version),
        ])
