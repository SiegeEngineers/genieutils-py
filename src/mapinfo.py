import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.mapelevation import MapElevation
from src.mapland import MapLand
from src.mapterrain import MapTerrain
from src.mapunit import MapUnit


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
