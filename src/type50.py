from dataclasses import dataclass

from src.attackorarmor import AttackOrArmor
from src.common import ByteHandler


@dataclass
class Type50(ByteHandler):
    base_armor: int
    attack_count: int
    attacks: list[AttackOrArmor]
    armour_count: int
    armours: list[AttackOrArmor]
    defense_terrain_bonus: int
    bonus_damage_resistance: float
    max_range: float
    blast_width: float
    reload_time: float
    projectile_unit_id: int
    accuracy_percent: int
    break_off_combat: int
    frame_delay: int
    graphic_displacement: list[float]
    blast_attack_level: int
    min_range: float
    accuracy_dispersion: float
    attack_graphic: int
    displayed_melee_armour: int
    displayed_attack: int
    displayed_range: float
    displayed_reload_time: float
    blast_damage: float

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.base_armor = self.read_int_16()
        self.attack_count = self.read_int_16()
        self.attacks = self.read_class_array(AttackOrArmor, self.attack_count)
        self.armour_count = self.read_int_16()
        self.armours = self.read_class_array(AttackOrArmor, self.armour_count)
        self.defense_terrain_bonus = self.read_int_16()
        self.bonus_damage_resistance = self.read_float()
        self.max_range = self.read_float()
        self.blast_width = self.read_float()
        self.reload_time = self.read_float()
        self.projectile_unit_id = self.read_int_16()
        self.accuracy_percent = self.read_int_16()
        self.break_off_combat = self.read_int_8()
        self.frame_delay = self.read_int_16()
        self.graphic_displacement = self.read_float_array(3)
        self.blast_attack_level = self.read_int_8()
        self.min_range = self.read_float()
        self.accuracy_dispersion = self.read_float()
        self.attack_graphic = self.read_int_16()
        self.displayed_melee_armour = self.read_int_16()
        self.displayed_attack = self.read_int_16()
        self.displayed_range = self.read_float()
        self.displayed_reload_time = self.read_float()
        self.blast_damage = self.read_float()
