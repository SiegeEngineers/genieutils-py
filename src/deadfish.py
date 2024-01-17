import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass


@dataclass
class DeadFish(GenieClass):
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

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'DeadFish':
        return cls(
            walking_graphic=content.read_int_16(),
            running_graphic=content.read_int_16(),
            rotation_speed=content.read_float(),
            old_size_class=content.read_int_8(),
            tracking_unit=content.read_int_16(),
            tracking_unit_mode=content.read_int_8(),
            tracking_unit_density=content.read_float(),
            old_move_algorithm=content.read_int_8(),
            turn_radius=content.read_float(),
            turn_radius_speed=content.read_float(),
            max_yaw_per_second_moving=content.read_float(),
            stationary_yaw_revolution_time=content.read_float(),
            max_yaw_per_second_stationary=content.read_float(),
            min_collision_size_multiplier=content.read_float(),
        )
