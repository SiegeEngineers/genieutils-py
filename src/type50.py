import typing
from dataclasses import dataclass

from src.attackorarmor import AttackOrArmor
from src.common import ByteHandler, GenieClass


@dataclass
class Type50(GenieClass):
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

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
        base_armor = content.read_int_16()
        attack_count = content.read_int_16()
        attacks = content.read_class_array(AttackOrArmor, attack_count)
        armour_count = content.read_int_16()
        armours = content.read_class_array(AttackOrArmor, armour_count)
        defense_terrain_bonus = content.read_int_16()
        bonus_damage_resistance = content.read_float()
        max_range = content.read_float()
        blast_width = content.read_float()
        reload_time = content.read_float()
        projectile_unit_id = content.read_int_16()
        accuracy_percent = content.read_int_16()
        break_off_combat = content.read_int_8()
        frame_delay = content.read_int_16()
        graphic_displacement = content.read_float_array(3)
        blast_attack_level = content.read_int_8()
        min_range = content.read_float()
        accuracy_dispersion = content.read_float()
        attack_graphic = content.read_int_16()
        displayed_melee_armour = content.read_int_16()
        displayed_attack = content.read_int_16()
        displayed_range = content.read_float()
        displayed_reload_time = content.read_float()
        blast_damage = content.read_float()
        return cls(
            base_armor=base_armor,
            attack_count=attack_count,
            attacks=attacks,
            armour_count=armour_count,
            armours=armours,
            defense_terrain_bonus=defense_terrain_bonus,
            bonus_damage_resistance=bonus_damage_resistance,
            max_range=max_range,
            blast_width=blast_width,
            reload_time=reload_time,
            projectile_unit_id=projectile_unit_id,
            accuracy_percent=accuracy_percent,
            break_off_combat=break_off_combat,
            frame_delay=frame_delay,
            graphic_displacement=graphic_displacement,
            blast_attack_level=blast_attack_level,
            min_range=min_range,
            accuracy_dispersion=accuracy_dispersion,
            attack_graphic=attack_graphic,
            displayed_melee_armour=displayed_melee_armour,
            displayed_attack=displayed_attack,
            displayed_range=displayed_range,
            displayed_reload_time=displayed_reload_time,
            blast_damage=blast_damage,
        )
