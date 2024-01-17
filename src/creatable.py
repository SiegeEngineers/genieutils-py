import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.resourcecost import ResourceCost


@dataclass
class Creatable(GenieClass):
    resource_costs: list[ResourceCost]
    train_time: int
    train_location_id: int
    button_id: int
    rear_attack_modifier: float
    flank_attack_modifier: float
    creatable_type: int
    hero_mode: int
    garrison_graphic: int
    spawning_graphic: int
    upgrade_graphic: int
    hero_glow_graphic: int
    max_charge: float
    recharge_rate: float
    charge_event: int
    charge_type: int
    min_conversion_time_mod: float
    max_conversion_time_mod: float
    conversion_chance_mod: float
    total_projectiles: float
    max_total_projectiles: int
    projectile_spawning_area: list[float]
    secondary_projectile_unit: int
    special_graphic: int
    special_ability: int
    displayed_pierce_armor: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Creatable':
        return cls(
            resource_costs=content.read_class_array(ResourceCost, 3),
            train_time=content.read_int_16(),
            train_location_id=content.read_int_16(),
            button_id=content.read_int_8(),
            rear_attack_modifier=content.read_float(),
            flank_attack_modifier=content.read_float(),
            creatable_type=content.read_int_8(),
            hero_mode=content.read_int_8(),
            garrison_graphic=content.read_int_32(),
            spawning_graphic=content.read_int_16(),
            upgrade_graphic=content.read_int_16(),
            hero_glow_graphic=content.read_int_16(),
            max_charge=content.read_float(),
            recharge_rate=content.read_float(),
            charge_event=content.read_int_16(),
            charge_type=content.read_int_16(),
            min_conversion_time_mod=content.read_float(),
            max_conversion_time_mod=content.read_float(),
            conversion_chance_mod=content.read_float(),
            total_projectiles=content.read_float(),
            max_total_projectiles=content.read_int_8(),
            projectile_spawning_area=content.read_float_array(3),
            secondary_projectile_unit=content.read_int_32(),
            special_graphic=content.read_int_32(),
            special_ability=content.read_int_8(),
            displayed_pierce_armor=content.read_int_16(),
        )
