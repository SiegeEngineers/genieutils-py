from dataclasses import dataclass

from src.common import ByteHandler
from src.mapelevation import MapElevation
from src.mapland import MapLand
from src.mapterrain import MapTerrain
from src.mapunit import MapUnit


@dataclass
class MapInfo(ByteHandler):
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

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.map_id = self.read_int_32()
        self.border_south_west = self.read_int_32()
        self.border_north_west = self.read_int_32()
        self.border_north_east = self.read_int_32()
        self.border_south_east = self.read_int_32()
        self.border_usage = self.read_int_32()
        self.water_shape = self.read_int_32()
        self.base_terrain = self.read_int_32()
        self.land_coverage = self.read_int_32()
        self.unused_id = self.read_int_32()
        self.map_lands_size = self.read_int_32(signed=False)
        self.map_lands_ptr = self.read_int_32()
        self.map_lands = self.read_map_lands_array(self.map_lands_size)
        self.map_terrains_size = self.read_int_32(signed=False)
        self.map_terrains_ptr = self.read_int_32()
        self.map_terrains = self.read_map_terrains_array(self.map_terrains_size)
        self.map_units_size = self.read_int_32(signed=False)
        self.map_units_ptr = self.read_int_32()
        self.map_units = self.read_map_units_array(self.map_units_size)
        self.map_elevations_size = self.read_int_32(signed=False)
        self.map_elevations_ptr = self.read_int_32()
        self.map_elevations = self.read_map_elevations_array(self.map_elevations_size)

    def read_map_lands_array(self, size: int) -> list[MapLand]:
        elements = []
        for i in range(size):
            map_land = MapLand(self.content[self.offset:])
            elements.append(map_land)
            self.offset += map_land.offset
        return elements

    def read_map_terrains_array(self, size: int) -> list[MapTerrain]:
        elements = []
        for i in range(size):
            map_terrain = MapTerrain(self.content[self.offset:])
            elements.append(map_terrain)
            self.offset += map_terrain.offset
        return elements

    def read_map_units_array(self, size: int) -> list[MapUnit]:
        elements = []
        for i in range(size):
            map_unit = MapUnit(self.content[self.offset:])
            elements.append(map_unit)
            self.offset += map_unit.offset
        return elements

    def read_map_elevations_array(self, size: int) -> list[MapElevation]:
        elements = []
        for i in range(size):
            map_elevation = MapElevation(self.content[self.offset:])
            elements.append(map_elevation)
            self.offset += map_elevation.offset
        return elements
