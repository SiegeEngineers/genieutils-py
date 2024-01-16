from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class DeadFish(ByteHandler):
    walking_graphic: int
    running_graphic: int
    rotation_speed: float
    old_size_class: int
    tracking_unit: int
    tracking_unit_mode: int
    tracking_unit_density: float
    old_move_algorithm: int
    turn_radius: float
    turn_radius_speed: float
    max_yaw_per_second_moving: float
    stationary_yaw_revolution_time: float
    max_yaw_per_second_stationary: float
    min_collision_size_multiplier: float

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.walking_graphic = self.read_int_16()
        self.running_graphic = self.read_int_16()
        self.rotation_speed = self.read_float()
        self.old_size_class = self.read_int_8()
        self.tracking_unit = self.read_int_16()
        self.tracking_unit_mode = self.read_int_8()
        self.tracking_unit_density = self.read_float()
        self.old_move_algorithm = self.read_int_8()
        self.turn_radius = self.read_float()
        self.turn_radius_speed = self.read_float()
        self.max_yaw_per_second_moving = self.read_float()
        self.stationary_yaw_revolution_time = self.read_float()
        self.max_yaw_per_second_stationary = self.read_float()
        self.min_collision_size_multiplier = self.read_float()
