from dataclasses import dataclass

from src.common import ByteHandler
from src.resourcecost import ResourceCost


@dataclass
class Creatable(ByteHandler):
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

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.resource_costs = self.read_resource_cost_array(3)
        self.train_time = self.read_int_16()
        self.train_location_id = self.read_int_16()
        self.button_id = self.read_int_8()
        self.rear_attack_modifier = self.read_float()
        self.flank_attack_modifier = self.read_float()
        self.creatable_type = self.read_int_8()
        self.hero_mode = self.read_int_8()
        self.garrison_graphic = self.read_int_32()
        self.spawning_graphic = self.read_int_16()
        self.upgrade_graphic = self.read_int_16()
        self.hero_glow_graphic = self.read_int_16()
        self.max_charge = self.read_float()
        self.recharge_rate = self.read_float()
        self.charge_event = self.read_int_16()
        self.charge_type = self.read_int_16()
        self.min_conversion_time_mod = self.read_float()
        self.max_conversion_time_mod = self.read_float()
        self.conversion_chance_mod = self.read_float()
        self.total_projectiles = self.read_float()
        self.max_total_projectiles = self.read_int_8()
        self.projectile_spawning_area = self.read_float_array(3)
        self.secondary_projectile_unit = self.read_int_32()
        self.special_graphic = self.read_int_32()
        self.special_ability = self.read_int_8()
        self.displayed_pierce_armor = self.read_int_16()

    def read_resource_cost_array(self, size: int) -> list[ResourceCost]:
        elements = []
        for i in range(size):
            resource_cost = ResourceCost(self.content[self.offset:])
            elements.append(resource_cost)
            self.offset += resource_cost.offset
        return elements
