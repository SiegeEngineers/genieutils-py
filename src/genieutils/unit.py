import struct
from dataclasses import dataclass

from genieutils.common import ByteHandler, UnitType, GenieClass
from genieutils.task import Task
from genieutils.versions import Version

RESOURCE_STORAGE_FORMAT = '<hfb'
RESOURCE_STORAGE_FORMAT_LENGTH = 7


@dataclass(slots=True)
class ResourceStorage(GenieClass):
    type: int
    amount: float
    flag: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'ResourceStorage':
        type_, amount, flag = struct.unpack(RESOURCE_STORAGE_FORMAT,
                                            content.consume_range(RESOURCE_STORAGE_FORMAT_LENGTH))
        return cls(
            type=type_,
            amount=amount,
            flag=flag,
        )

    def to_bytes(self, version: Version) -> bytes:
        return struct.pack(RESOURCE_STORAGE_FORMAT, self.type, self.amount, self.flag)


DAMAGE_GRAPHIC_FORMAT = '<hhb'
DAMAGE_GRAPHIC_FORMAT_LENGTH = 5


@dataclass(slots=True)
class DamageGraphic(GenieClass):
    graphic_id: int
    damage_percent: int
    apply_mode: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'DamageGraphic':
        graphic_id, \
            damage_percent, \
            apply_mode = struct.unpack(DAMAGE_GRAPHIC_FORMAT, content.consume_range(DAMAGE_GRAPHIC_FORMAT_LENGTH))
        return cls(
            graphic_id=graphic_id,
            damage_percent=damage_percent,
            apply_mode=apply_mode,
        )

    def to_bytes(self, version: Version) -> bytes:
        return struct.pack(DAMAGE_GRAPHIC_FORMAT, self.graphic_id, self.damage_percent, self.apply_mode)


DEAD_FISH_FORMAT = '<hhfbhbfbffffff'
DEAD_FISH_FORMAT_LENGTH = 41


@dataclass(slots=True)
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
        walking_graphic, \
            running_graphic, \
            rotation_speed, \
            old_size_class, \
            tracking_unit, \
            tracking_unit_mode, \
            tracking_unit_density, \
            old_move_algorithm, \
            turn_radius, \
            turn_radius_speed, \
            max_yaw_per_second_moving, \
            stationary_yaw_revolution_time, \
            max_yaw_per_second_stationary, \
            min_collision_size_multiplier = struct.unpack(DEAD_FISH_FORMAT,
                                                          content.consume_range(DEAD_FISH_FORMAT_LENGTH))
        return cls(
            walking_graphic=walking_graphic,
            running_graphic=running_graphic,
            rotation_speed=rotation_speed,
            old_size_class=old_size_class,
            tracking_unit=tracking_unit,
            tracking_unit_mode=tracking_unit_mode,
            tracking_unit_density=tracking_unit_density,
            old_move_algorithm=old_move_algorithm,
            turn_radius=turn_radius,
            turn_radius_speed=turn_radius_speed,
            max_yaw_per_second_moving=max_yaw_per_second_moving,
            stationary_yaw_revolution_time=stationary_yaw_revolution_time,
            max_yaw_per_second_stationary=max_yaw_per_second_stationary,
            min_collision_size_multiplier=min_collision_size_multiplier,
        )

    def to_bytes(self, version: Version) -> bytes:
        return struct.pack(DEAD_FISH_FORMAT,
                           self.walking_graphic,
                           self.running_graphic,
                           self.rotation_speed,
                           self.old_size_class,
                           self.tracking_unit,
                           self.tracking_unit_mode,
                           self.tracking_unit_density,
                           self.old_move_algorithm,
                           self.turn_radius,
                           self.turn_radius_speed,
                           self.max_yaw_per_second_moving,
                           self.stationary_yaw_revolution_time,
                           self.max_yaw_per_second_stationary,
                           self.min_collision_size_multiplier
                           )


@dataclass(slots=True)
class Bird(GenieClass):
    default_task_id: int
    search_radius: float
    work_rate: float
    drop_sites: list[int]
    task_swap_group: int
    attack_sound: int
    move_sound: int
    wwise_attack_sound_id: int
    wwise_move_sound_id: int
    run_pattern: int
    tasks: list[Task]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Bird':
        default_task_id = content.read_int_16()
        search_radius = content.read_float()
        work_rate = content.read_float()
        drop_sites_size = 3
        if content.version > Version.VER_77:
            drop_sites_size = content.read_int_16()
        drop_sites = content.read_int_16_array(drop_sites_size)
        task_swap_group = content.read_int_8()
        attack_sound = content.read_int_16()
        move_sound = content.read_int_16()
        wwise_attack_sound_id = content.read_int_32()
        wwise_move_sound_id = content.read_int_32()
        run_pattern = content.read_int_8()
        task_size = content.read_int_16()
        tasks = content.read_class_array(Task, task_size)
        return cls(
            default_task_id=default_task_id,
            search_radius=search_radius,
            work_rate=work_rate,
            drop_sites=drop_sites,
            task_swap_group=task_swap_group,
            attack_sound=attack_sound,
            move_sound=move_sound,
            wwise_attack_sound_id=wwise_attack_sound_id,
            wwise_move_sound_id=wwise_move_sound_id,
            run_pattern=run_pattern,
            tasks=tasks,
        )

    def to_bytes(self, version: Version) -> bytes:
        return b''.join([
            self.write_int_16(self.default_task_id),
            self.write_float(self.search_radius),
            self.write_float(self.work_rate),
            self.write_int_16(len(self.drop_sites), if_=(version >= Version.VER_78)),
            self.write_int_16_array(self.drop_sites),
            self.write_int_8(self.task_swap_group),
            self.write_int_16(self.attack_sound),
            self.write_int_16(self.move_sound),
            self.write_int_32(self.wwise_attack_sound_id),
            self.write_int_32(self.wwise_move_sound_id),
            self.write_int_8(self.run_pattern),
            self.write_int_16(len(self.tasks)),
            self.write_class_array(self.tasks, version),
        ])


ATTACK_OR_ARMOR_FORMAT = '<hh'
ATTACK_OR_ARMOR_FORMAT_LENGTH = 4


@dataclass(slots=True)
class AttackOrArmor(GenieClass):
    class_: int
    amount: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'AttackOrArmor':
        class_, amount = struct.unpack(ATTACK_OR_ARMOR_FORMAT, content.consume_range(ATTACK_OR_ARMOR_FORMAT_LENGTH))
        return cls(
            class_=class_,
            amount=amount,
        )

    def to_bytes(self, version: Version) -> bytes:
        return struct.pack(ATTACK_OR_ARMOR_FORMAT, self.class_, self.amount)


@dataclass(slots=True)
class Type50(GenieClass):
    base_armor: int
    attacks: list[AttackOrArmor]
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
    graphic_displacement: tuple[float, float, float]
    blast_attack_level: int
    min_range: float
    accuracy_dispersion: float
    attack_graphic: int
    displayed_melee_armour: int
    displayed_attack: int
    displayed_range: float
    displayed_reload_time: float
    blast_damage: float
    damage_reflection: float
    friendly_fire_damage: float
    interrupt_frame: int
    garrison_firepower: float
    attack_graphic_2: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Type50':
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
        graphic_displacement = content.read_float_array_3()
        blast_attack_level = content.read_int_8()
        min_range = content.read_float()
        accuracy_dispersion = content.read_float()
        attack_graphic = content.read_int_16()
        displayed_melee_armour = content.read_int_16()
        displayed_attack = content.read_int_16()
        displayed_range = content.read_float()
        displayed_reload_time = content.read_float()
        blast_damage = content.read_float()
        damage_reflection = 0.0
        friendly_fire_damage = 1.0
        interrupt_frame = -1
        garrison_firepower = 0.0
        attack_graphic_2 = -1
        if content.version >= Version.VER_84:
            damage_reflection = content.read_float()
            friendly_fire_damage = content.read_float()
            interrupt_frame = content.read_int_16()
            garrison_firepower = content.read_float()
            attack_graphic_2 = content.read_int_16()
        return cls(
            base_armor=base_armor,
            attacks=attacks,
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
            damage_reflection=damage_reflection,
            friendly_fire_damage=friendly_fire_damage,
            interrupt_frame=interrupt_frame,
            garrison_firepower=garrison_firepower,
            attack_graphic_2=attack_graphic_2,
        )

    def to_bytes(self, version: Version) -> bytes:
        value = b''.join([
            self.write_int_16(self.base_armor),
            self.write_int_16(len(self.attacks)),
            self.write_class_array(self.attacks, version),
            self.write_int_16(len(self.armours)),
            self.write_class_array(self.armours, version),
            self.write_int_16(self.defense_terrain_bonus),
            self.write_float(self.bonus_damage_resistance),
            self.write_float(self.max_range),
            self.write_float(self.blast_width),
            self.write_float(self.reload_time),
            self.write_int_16(self.projectile_unit_id),
            self.write_int_16(self.accuracy_percent),
            self.write_int_8(self.break_off_combat),
            self.write_int_16(self.frame_delay),
            self.write_float_array(self.graphic_displacement),
            self.write_int_8(self.blast_attack_level),
            self.write_float(self.min_range),
            self.write_float(self.accuracy_dispersion),
            self.write_int_16(self.attack_graphic),
            self.write_int_16(self.displayed_melee_armour),
            self.write_int_16(self.displayed_attack),
            self.write_float(self.displayed_range),
            self.write_float(self.displayed_reload_time),
            self.write_float(self.blast_damage),
        ])
        if version >= Version.VER_84:
            value += b''.join([
                self.write_float(self.damage_reflection),
                self.write_float(self.friendly_fire_damage),
                self.write_int_16(self.interrupt_frame),
                self.write_float(self.garrison_firepower),
                self.write_int_16(self.attack_graphic_2),
            ])
        return value


PROJECTILE_FORMAT = '<bbbbbf'
PROJECTILE_FORMAT_LENGTH = 9


@dataclass(slots=True)
class Projectile(GenieClass):
    projectile_type: int
    smart_mode: int
    hit_mode: int
    vanish_mode: int
    area_effect_specials: int
    projectile_arc: float

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Projectile':
        projectile_type, \
            smart_mode, \
            hit_mode, \
            vanish_mode, \
            area_effect_specials, \
            projectile_arc = struct.unpack(PROJECTILE_FORMAT, content.consume_range(PROJECTILE_FORMAT_LENGTH))
        return cls(
            projectile_type=projectile_type,
            smart_mode=smart_mode,
            hit_mode=hit_mode,
            vanish_mode=vanish_mode,
            area_effect_specials=area_effect_specials,
            projectile_arc=projectile_arc,
        )

    def to_bytes(self, version: Version) -> bytes:
        return struct.pack(PROJECTILE_FORMAT,
                           self.projectile_type,
                           self.smart_mode,
                           self.hit_mode,
                           self.vanish_mode,
                           self.area_effect_specials,
                           self.projectile_arc,
                           )


RESOURCE_COST_FORMAT = '<hhh'
RESOURCE_COST_FORMAT_LENGTH = 6


@dataclass(slots=True)
class ResourceCost(GenieClass):
    type: int
    amount: int
    flag: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'ResourceCost':
        type_, amount, flag = struct.unpack(RESOURCE_COST_FORMAT, content.consume_range(RESOURCE_COST_FORMAT_LENGTH))
        return cls(
            type=type_,
            amount=amount,
            flag=flag,
        )

    def to_bytes(self, version: Version) -> bytes:
        return struct.pack(RESOURCE_COST_FORMAT, self.type, self.amount, self.flag)


TRAIN_LOCATION_FORMAT = '<hhb'
TRAIN_LOCATOIN_FORMAT_LENGTH = struct.calcsize(TRAIN_LOCATION_FORMAT)

TRAIN_LOCATION_FORMAT_88 = '<hhbl'
TRAIN_LOCATOIN_FORMAT_LENGTH_88 = struct.calcsize(TRAIN_LOCATION_FORMAT_88)


@dataclass(slots=True)
class TrainLocation(GenieClass):
    train_time: int
    unit_id: int
    button_id: int
    hot_key_id: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'TrainLocation':
        if content.version >= Version.VER_88:
            return cls.from_bytes_88(content)
        return cls.from_bytes_84(content)

    @classmethod
    def from_bytes_84(cls, content: ByteHandler) -> 'TrainLocation':
        train_time, \
            unit_id, \
            button_id = struct.unpack(TRAIN_LOCATION_FORMAT, content.consume_range(TRAIN_LOCATOIN_FORMAT_LENGTH))
        return cls(
            train_time=train_time,
            unit_id=unit_id,
            button_id=button_id,
            hot_key_id=16_000,
        )

    @classmethod
    def from_bytes_88(cls, content: ByteHandler) -> 'TrainLocation':
        train_time, \
            unit_id, \
            button_id, \
            hot_key_id = struct.unpack(TRAIN_LOCATION_FORMAT_88, content.consume_range(TRAIN_LOCATOIN_FORMAT_LENGTH_88))
        return cls(
            train_time=train_time,
            unit_id=unit_id,
            button_id=button_id,
            hot_key_id=hot_key_id,
        )

    def to_bytes(self, version: Version) -> bytes:
        if version >= Version.VER_88:
            return struct.pack(TRAIN_LOCATION_FORMAT_88, self.train_time, self.unit_id, self.button_id, self.hot_key_id)
        return struct.pack(TRAIN_LOCATION_FORMAT, self.train_time, self.unit_id, self.button_id)


CREATABLE_FORMAT = '<hhbffbblhhhffhhffffbfffllbh'
CREATABLE_FORMAT_LENGTH = 77
CREATABLE_FORMAT_84 = '<hhbffbblhhhhffhhhlbfhllhffffbfffllbh'
CREATABLE_FORMAT_LENGTH_84 = struct.calcsize(CREATABLE_FORMAT_84)
CREATABLE_FORMAT_88 = '<ffbblhhhhffhhhlbfhllhffffbfffllbh'
CREATABLE_FORMAT_LENGTH_88 = struct.calcsize(CREATABLE_FORMAT_88)


@dataclass(slots=True)
class Creatable(GenieClass):
    resource_costs: tuple[ResourceCost, ResourceCost, ResourceCost]
    train_locations: list[TrainLocation]
    rear_attack_modifier: float
    flank_attack_modifier: float
    creatable_type: int
    hero_mode: int
    garrison_graphic: int
    spawning_graphic: int
    upgrade_graphic: int
    hero_glow_graphic: int
    idle_attack_graphic: int
    max_charge: float
    recharge_rate: float
    charge_event: int
    charge_type: int
    charge_target: int
    charge_projectile_unit: int
    attack_priority: int
    invulnerability_level: float
    button_icon_id: int
    button_short_tooltip_id: int
    button_extended_tooltip_id: int
    button_hotkey_action: int
    min_conversion_time_mod: float
    max_conversion_time_mod: float
    conversion_chance_mod: float
    total_projectiles: float
    max_total_projectiles: int
    projectile_spawning_area: tuple[float, float, float]
    secondary_projectile_unit: int
    special_graphic: int
    special_ability: int
    displayed_pierce_armour: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Creatable':
        if content.version >= Version.VER_88:
            return cls.from_bytes_88(content)
        elif content.version >= Version.VER_84:
            return cls.from_bytes_84(content)
        return cls.from_bytes_78(content)

    @classmethod
    def from_bytes_78(cls, content: ByteHandler) -> 'Creatable':
        resource_costs = content.read_class_array_3(ResourceCost)
        train_time, \
            train_location_id, \
            button_id, \
            rear_attack_modifier, \
            flank_attack_modifier, \
            creatable_type, \
            hero_mode, \
            garrison_graphic, \
            spawning_graphic, \
            upgrade_graphic, \
            hero_glow_graphic, \
            max_charge, \
            recharge_rate, \
            charge_event, \
            charge_type, \
            min_conversion_time_mod, \
            max_conversion_time_mod, \
            conversion_chance_mod, \
            total_projectiles, \
            max_total_projectiles, \
            projectile_spawning_area_1, \
            projectile_spawning_area_2, \
            projectile_spawning_area_3, \
            secondary_projectile_unit, \
            special_graphic, \
            special_ability, \
            displayed_pierce_armour = struct.unpack(CREATABLE_FORMAT, content.consume_range(CREATABLE_FORMAT_LENGTH))
        idle_attack_graphic = -1
        charge_target = 0
        charge_projectile_unit = -1
        attack_priority = 0
        invulnerability_level = 0
        button_icon_id = -1
        button_short_tooltip_id = -1
        button_extended_tooltip_id = -1
        button_hotkey_action = -1
        train_locations = [
            TrainLocation(train_time=train_time, unit_id=train_location_id, button_id=button_id, hot_key_id=16000),
        ]
        return cls(
            resource_costs=resource_costs,
            train_locations=train_locations,
            rear_attack_modifier=rear_attack_modifier,
            flank_attack_modifier=flank_attack_modifier,
            creatable_type=creatable_type,
            hero_mode=hero_mode,
            garrison_graphic=garrison_graphic,
            spawning_graphic=spawning_graphic,
            upgrade_graphic=upgrade_graphic,
            hero_glow_graphic=hero_glow_graphic,
            idle_attack_graphic=idle_attack_graphic,
            max_charge=max_charge,
            recharge_rate=recharge_rate,
            charge_event=charge_event,
            charge_type=charge_type,
            charge_target=charge_target,
            charge_projectile_unit=charge_projectile_unit,
            attack_priority=attack_priority,
            invulnerability_level=invulnerability_level,
            button_icon_id=button_icon_id,
            button_short_tooltip_id=button_short_tooltip_id,
            button_extended_tooltip_id=button_extended_tooltip_id,
            button_hotkey_action=button_hotkey_action,
            min_conversion_time_mod=min_conversion_time_mod,
            max_conversion_time_mod=max_conversion_time_mod,
            conversion_chance_mod=conversion_chance_mod,
            total_projectiles=total_projectiles,
            max_total_projectiles=max_total_projectiles,
            projectile_spawning_area=(
                projectile_spawning_area_1,
                projectile_spawning_area_2,
                projectile_spawning_area_3),
            secondary_projectile_unit=secondary_projectile_unit,
            special_graphic=special_graphic,
            special_ability=special_ability,
            displayed_pierce_armour=displayed_pierce_armour,
        )

    @classmethod
    def from_bytes_84(cls, content: ByteHandler) -> 'Creatable':
        resource_costs = content.read_class_array_3(ResourceCost)
        train_time, \
            train_location_id, \
            button_id, \
            rear_attack_modifier, \
            flank_attack_modifier, \
            creatable_type, \
            hero_mode, \
            garrison_graphic, \
            spawning_graphic, \
            upgrade_graphic, \
            hero_glow_graphic, \
            idle_attack_graphic, \
            max_charge, \
            recharge_rate, \
            charge_event, \
            charge_type, \
            charge_target, \
            charge_projectile_unit, \
            attack_priority, \
            invulnerability_level, \
            button_icon_id, \
            button_short_tooltip_id, \
            button_extended_tooltip_id, \
            button_hotkey_action, \
            min_conversion_time_mod, \
            max_conversion_time_mod, \
            conversion_chance_mod, \
            total_projectiles, \
            max_total_projectiles, \
            projectile_spawning_area_1, \
            projectile_spawning_area_2, \
            projectile_spawning_area_3, \
            secondary_projectile_unit, \
            special_graphic, \
            special_ability, \
            displayed_pierce_armour = struct.unpack(CREATABLE_FORMAT_84,
                                                   content.consume_range(CREATABLE_FORMAT_LENGTH_84))
        train_locations = [
            TrainLocation(train_time=train_time, unit_id=train_location_id, button_id=button_id, hot_key_id=16000),
        ]
        return cls(
            resource_costs=resource_costs,
            train_locations=train_locations,
            rear_attack_modifier=rear_attack_modifier,
            flank_attack_modifier=flank_attack_modifier,
            creatable_type=creatable_type,
            hero_mode=hero_mode,
            garrison_graphic=garrison_graphic,
            spawning_graphic=spawning_graphic,
            upgrade_graphic=upgrade_graphic,
            hero_glow_graphic=hero_glow_graphic,
            idle_attack_graphic=idle_attack_graphic,
            max_charge=max_charge,
            recharge_rate=recharge_rate,
            charge_event=charge_event,
            charge_type=charge_type,
            charge_target=charge_target,
            charge_projectile_unit=charge_projectile_unit,
            attack_priority=attack_priority,
            invulnerability_level=invulnerability_level,
            button_icon_id=button_icon_id,
            button_short_tooltip_id=button_short_tooltip_id,
            button_extended_tooltip_id=button_extended_tooltip_id,
            button_hotkey_action=button_hotkey_action,
            min_conversion_time_mod=min_conversion_time_mod,
            max_conversion_time_mod=max_conversion_time_mod,
            conversion_chance_mod=conversion_chance_mod,
            total_projectiles=total_projectiles,
            max_total_projectiles=max_total_projectiles,
            projectile_spawning_area=(
                projectile_spawning_area_1,
                projectile_spawning_area_2,
                projectile_spawning_area_3),
            secondary_projectile_unit=secondary_projectile_unit,
            special_graphic=special_graphic,
            special_ability=special_ability,
            displayed_pierce_armour=displayed_pierce_armour,
        )

    @classmethod
    def from_bytes_88(cls, content: ByteHandler) -> 'Creatable':
        resource_costs = content.read_class_array_3(ResourceCost)
        train_location_count = content.read_int_16()
        train_locations = content.read_class_array(TrainLocation, train_location_count)
        rear_attack_modifier, \
            flank_attack_modifier, \
            creatable_type, \
            hero_mode, \
            garrison_graphic, \
            spawning_graphic, \
            upgrade_graphic, \
            hero_glow_graphic, \
            idle_attack_graphic, \
            max_charge, \
            recharge_rate, \
            charge_event, \
            charge_type, \
            charge_target, \
            charge_projectile_unit, \
            attack_priority, \
            invulnerability_level, \
            button_icon_id, \
            button_short_tooltip_id, \
            button_extended_tooltip_id, \
            button_hotkey_action, \
            min_conversion_time_mod, \
            max_conversion_time_mod, \
            conversion_chance_mod, \
            total_projectiles, \
            max_total_projectiles, \
            projectile_spawning_area_1, \
            projectile_spawning_area_2, \
            projectile_spawning_area_3, \
            secondary_projectile_unit, \
            special_graphic, \
            special_ability, \
            displayed_pierce_armour = struct.unpack(CREATABLE_FORMAT_88,
                                                   content.consume_range(CREATABLE_FORMAT_LENGTH_88))
        return cls(
            resource_costs=resource_costs,
            train_locations=train_locations,
            rear_attack_modifier=rear_attack_modifier,
            flank_attack_modifier=flank_attack_modifier,
            creatable_type=creatable_type,
            hero_mode=hero_mode,
            garrison_graphic=garrison_graphic,
            spawning_graphic=spawning_graphic,
            upgrade_graphic=upgrade_graphic,
            hero_glow_graphic=hero_glow_graphic,
            idle_attack_graphic=idle_attack_graphic,
            max_charge=max_charge,
            recharge_rate=recharge_rate,
            charge_event=charge_event,
            charge_type=charge_type,
            charge_target=charge_target,
            charge_projectile_unit=charge_projectile_unit,
            attack_priority=attack_priority,
            invulnerability_level=invulnerability_level,
            button_icon_id=button_icon_id,
            button_short_tooltip_id=button_short_tooltip_id,
            button_extended_tooltip_id=button_extended_tooltip_id,
            button_hotkey_action=button_hotkey_action,
            min_conversion_time_mod=min_conversion_time_mod,
            max_conversion_time_mod=max_conversion_time_mod,
            conversion_chance_mod=conversion_chance_mod,
            total_projectiles=total_projectiles,
            max_total_projectiles=max_total_projectiles,
            projectile_spawning_area=(
                projectile_spawning_area_1,
                projectile_spawning_area_2,
                projectile_spawning_area_3),
            secondary_projectile_unit=secondary_projectile_unit,
            special_graphic=special_graphic,
            special_ability=special_ability,
            displayed_pierce_armour=displayed_pierce_armour,
        )

    def to_bytes(self, version: Version) -> bytes:
        if version >= Version.VER_88:
            return self.to_bytes_88(version)
        if version >= Version.VER_84:
            return self.to_bytes_84(version)
        return self.to_bytes_78(version)

    def to_bytes_78(self, version: Version) -> bytes:
        return self.write_class_array(self.resource_costs, version) + \
            struct.pack(CREATABLE_FORMAT,
                        self.train_locations[0].train_time,
                        self.train_locations[0].unit_id,
                        self.train_locations[0].button_id,
                        self.rear_attack_modifier,
                        self.flank_attack_modifier,
                        self.creatable_type,
                        self.hero_mode,
                        self.garrison_graphic,
                        self.spawning_graphic,
                        self.upgrade_graphic,
                        self.hero_glow_graphic,
                        self.max_charge,
                        self.recharge_rate,
                        self.charge_event,
                        self.charge_type,
                        self.min_conversion_time_mod,
                        self.max_conversion_time_mod,
                        self.conversion_chance_mod,
                        self.total_projectiles,
                        self.max_total_projectiles,
                        *self.projectile_spawning_area,
                        self.secondary_projectile_unit,
                        self.special_graphic,
                        self.special_ability,
                        self.displayed_pierce_armour,
                        )

    def to_bytes_84(self, version: Version) -> bytes:
        return self.write_class_array(self.resource_costs, version) + \
            struct.pack(CREATABLE_FORMAT_84,
                        self.train_locations[0].train_time,
                        self.train_locations[0].unit_id,
                        self.train_locations[0].button_id,
                        self.rear_attack_modifier,
                        self.flank_attack_modifier,
                        self.creatable_type,
                        self.hero_mode,
                        self.garrison_graphic,
                        self.spawning_graphic,
                        self.upgrade_graphic,
                        self.hero_glow_graphic,
                        self.idle_attack_graphic,
                        self.max_charge,
                        self.recharge_rate,
                        self.charge_event,
                        self.charge_type,
                        self.charge_target,
                        self.charge_projectile_unit,
                        self.attack_priority,
                        self.invulnerability_level,
                        self.button_icon_id,
                        self.button_short_tooltip_id,
                        self.button_extended_tooltip_id,
                        self.button_hotkey_action,
                        self.min_conversion_time_mod,
                        self.max_conversion_time_mod,
                        self.conversion_chance_mod,
                        self.total_projectiles,
                        self.max_total_projectiles,
                        *self.projectile_spawning_area,
                        self.secondary_projectile_unit,
                        self.special_graphic,
                        self.special_ability,
                        self.displayed_pierce_armour,
                        )

    def to_bytes_88(self, version: Version) -> bytes:
        return self.write_class_array(self.resource_costs, version) + \
        self.write_int_16(len(self.train_locations)) + \
        self.write_class_array(self.train_locations, version) + \
            struct.pack(CREATABLE_FORMAT_88,
                        self.rear_attack_modifier,
                        self.flank_attack_modifier,
                        self.creatable_type,
                        self.hero_mode,
                        self.garrison_graphic,
                        self.spawning_graphic,
                        self.upgrade_graphic,
                        self.hero_glow_graphic,
                        self.idle_attack_graphic,
                        self.max_charge,
                        self.recharge_rate,
                        self.charge_event,
                        self.charge_type,
                        self.charge_target,
                        self.charge_projectile_unit,
                        self.attack_priority,
                        self.invulnerability_level,
                        self.button_icon_id,
                        self.button_short_tooltip_id,
                        self.button_extended_tooltip_id,
                        self.button_hotkey_action,
                        self.min_conversion_time_mod,
                        self.max_conversion_time_mod,
                        self.conversion_chance_mod,
                        self.total_projectiles,
                        self.max_total_projectiles,
                        *self.projectile_spawning_area,
                        self.secondary_projectile_unit,
                        self.special_graphic,
                        self.special_ability,
                        self.displayed_pierce_armour,
                        )


BUILDING_ANNEX_FORMAT = '<hff'
BUILDING_ANNEX_FORMAT_LENGTH = 10


@dataclass(slots=True)
class BuildingAnnex(GenieClass):
    unit_id: int
    misplacement_x: float
    misplacement_y: float

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'BuildingAnnex':
        unit_id, misplacement_x, misplacement_y = struct.unpack(BUILDING_ANNEX_FORMAT,
                                                                content.consume_range(BUILDING_ANNEX_FORMAT_LENGTH))
        return cls(
            unit_id=unit_id,
            misplacement_x=misplacement_x,
            misplacement_y=misplacement_y,
        )

    def to_bytes(self, version: Version) -> bytes:
        return struct.pack(BUILDING_ANNEX_FORMAT,
                           self.unit_id,
                           self.misplacement_x,
                           self.misplacement_y,
                           )


BUILDING_ANNEX_FORMAT_1 = '<hhhhhhbhbhhhhb'
BUILDING_ANNEX_FORMAT_1_LENGTH = 25

BUILDING_ANNEX_FORMAT_2 = '<hhhhllbffhbbbbbb'
BUILDING_ANNEX_FORMAT_2_LENGTH = 33


@dataclass(slots=True)
class Building(GenieClass):
    construction_graphic_id: int
    snow_graphic_id: int
    destruction_graphic_id: int
    destruction_rubble_graphic_id: int
    researching_graphic: int
    research_completed_graphic: int
    adjacent_mode: int
    graphics_angle: int
    disappears_when_built: int
    stack_unit_id: int
    foundation_terrain_id: int
    old_overlap_id: int
    tech_id: int
    can_burn: int
    annexes: tuple[BuildingAnnex, BuildingAnnex, BuildingAnnex, BuildingAnnex]
    head_unit: int
    transform_unit: int
    transform_sound: int
    construction_sound: int
    wwise_transform_sound_id: int
    wwise_construction_sound_id: int
    garrison_type: int
    garrison_heal_rate: float
    garrison_repair_rate: float
    pile_unit: int
    looting_table: tuple[int, int, int, int, int, int]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Building':
        construction_graphic_id, \
            snow_graphic_id, \
            destruction_graphic_id, \
            destruction_rubble_graphic_id, \
            researching_graphic, \
            research_completed_graphic, \
            adjacent_mode, \
            graphics_angle, \
            disappears_when_built, \
            stack_unit_id, \
            foundation_terrain_id, \
            old_overlap_id, \
            tech_id, \
            can_burn = struct.unpack(BUILDING_ANNEX_FORMAT_1, content.consume_range(BUILDING_ANNEX_FORMAT_1_LENGTH))

        annexes = content.read_class_array_4(BuildingAnnex)

        head_unit, \
            transform_unit, \
            transform_sound, \
            construction_sound, \
            wwise_transform_sound_id, \
            wwise_construction_sound_id, \
            garrison_type, \
            garrison_heal_rate, \
            garrison_repair_rate, \
            pile_unit, \
            looting_table_1, \
            looting_table_2, \
            looting_table_3, \
            looting_table_4, \
            looting_table_5, \
            looting_table_6 = struct.unpack(BUILDING_ANNEX_FORMAT_2,
                                            content.consume_range(BUILDING_ANNEX_FORMAT_2_LENGTH))

        return cls(
            construction_graphic_id=construction_graphic_id,
            snow_graphic_id=snow_graphic_id,
            destruction_graphic_id=destruction_graphic_id,
            destruction_rubble_graphic_id=destruction_rubble_graphic_id,
            researching_graphic=researching_graphic,
            research_completed_graphic=research_completed_graphic,
            adjacent_mode=adjacent_mode,
            graphics_angle=graphics_angle,
            disappears_when_built=disappears_when_built,
            stack_unit_id=stack_unit_id,
            foundation_terrain_id=foundation_terrain_id,
            old_overlap_id=old_overlap_id,
            tech_id=tech_id,
            can_burn=can_burn,
            annexes=annexes,
            head_unit=head_unit,
            transform_unit=transform_unit,
            transform_sound=transform_sound,
            construction_sound=construction_sound,
            wwise_transform_sound_id=wwise_transform_sound_id,
            wwise_construction_sound_id=wwise_construction_sound_id,
            garrison_type=garrison_type,
            garrison_heal_rate=garrison_heal_rate,
            garrison_repair_rate=garrison_repair_rate,
            pile_unit=pile_unit,
            looting_table=(
                looting_table_1,
                looting_table_2,
                looting_table_3,
                looting_table_4,
                looting_table_5,
                looting_table_6,
            ),
        )

    def to_bytes(self, version: Version) -> bytes:
        return struct.pack(BUILDING_ANNEX_FORMAT_1,
                           self.construction_graphic_id,
                           self.snow_graphic_id,
                           self.destruction_graphic_id,
                           self.destruction_rubble_graphic_id,
                           self.researching_graphic,
                           self.research_completed_graphic,
                           self.adjacent_mode,
                           self.graphics_angle,
                           self.disappears_when_built,
                           self.stack_unit_id,
                           self.foundation_terrain_id,
                           self.old_overlap_id,
                           self.tech_id,
                           self.can_burn,
                           ) + \
            self.write_class_array(self.annexes, version) + \
            struct.pack(BUILDING_ANNEX_FORMAT_2,
                        self.head_unit,
                        self.transform_unit,
                        self.transform_sound,
                        self.construction_sound,
                        self.wwise_transform_sound_id,
                        self.wwise_construction_sound_id,
                        self.garrison_type,
                        self.garrison_heal_rate,
                        self.garrison_repair_rate,
                        self.pile_unit,
                        *self.looting_table,
                        )


FORMAT = ('<bhllhhhhhbhfbfffhhhhbbhbhbbhhhhffbbhbhfbbbbbfblllbbbbbbbbbhbbfffll')
FORMAT_LENGTH = 140

FORMAT_88 = ('<bhllhhhhhbhfbfffhhhhbbhbhbbhhhhffbbhbhfbbbbbfbllbbbbbbbbbhbbfffll')
FORMAT_LENGTH_88 = struct.calcsize(FORMAT_88)


@dataclass(slots=True)
class Unit(GenieClass):
    type: int
    id: int
    language_dll_name: int
    language_dll_creation: int
    class_: int
    standing_graphic: tuple[int, int]
    dying_graphic: int
    undead_graphic: int
    undead_mode: int
    hit_points: int
    line_of_sight: float
    garrison_capacity: int
    collision_size_x: float
    collision_size_y: float
    collision_size_z: float
    train_sound: int
    damage_sound: int
    dead_unit_id: int
    blood_unit_id: int
    sort_number: int
    can_be_built_on: int
    icon_id: int
    hide_in_editor: int
    old_portrait_pict: int
    enabled: int
    disabled: int
    placement_side_terrain: tuple[int, int]
    placement_terrain: tuple[int, int]
    clearance_size: tuple[float, float]
    hill_mode: int
    fog_visibility: int
    terrain_restriction: int
    fly_mode: int
    resource_capacity: int
    resource_decay: float
    blast_defense_level: int
    combat_level: int
    interaction_mode: int
    minimap_mode: int
    interface_kind: int
    multiple_attribute_mode: float
    minimap_color: int
    language_dll_help: int
    language_dll_hotkey_text: int
    hot_key: int
    recyclable: int
    enable_auto_gather: int
    create_doppelganger_on_death: int
    resource_gather_group: int
    occlusion_mode: int
    obstruction_type: int
    obstruction_class: int
    trait: int
    civilization: int
    nothing: int
    selection_effect: int
    editor_selection_colour: int
    outline_size_x: float
    outline_size_y: float
    outline_size_z: float
    scenario_triggers_1: int
    scenario_triggers_2: int
    resource_storages: tuple[ResourceStorage, ResourceStorage, ResourceStorage]
    damage_graphics: list[DamageGraphic]
    selection_sound: int
    dying_sound: int
    wwise_train_sound_id: int
    wwise_damage_sound_id: int
    wwise_selection_sound_id: int
    wwise_dying_sound_id: int
    old_attack_reaction: int
    convert_terrain: int
    name: str
    copy_id: int
    base_id: int
    speed: float | None = None
    dead_fish: DeadFish | None = None
    bird: Bird | None = None
    type_50: Type50 | None = None
    projectile: Projectile | None = None
    creatable: Creatable | None = None
    building: Building | None = None

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Unit':
        if content.version >= Version.VER_88:
            return cls.from_bytes_88(content)
        return cls.from_bytes_84(content)

    @classmethod
    def from_bytes_84(cls, content: ByteHandler) -> 'Unit':
        type_, \
            id_, \
            language_dll_name, \
            language_dll_creation, \
            class_, \
            standing_graphic_1, standing_graphic_2, \
            dying_graphic, \
            undead_graphic, \
            undead_mode, \
            hit_points, \
            line_of_sight, \
            garrison_capacity, \
            collision_size_x, \
            collision_size_y, \
            collision_size_z, \
            train_sound, \
            damage_sound, \
            dead_unit_id, \
            blood_unit_id, \
            sort_number, \
            can_be_built_on, \
            icon_id, \
            hide_in_editor, \
            old_portrait_pict, \
            enabled, \
            disabled, \
            placement_side_terrain_1, placement_side_terrain_2, \
            placement_terrain_1, placement_terrain_2, \
            clearance_size_1, clearance_size_2, \
            hill_mode, \
            fog_visibility, \
            terrain_restriction, \
            fly_mode, \
            resource_capacity, \
            resource_decay, \
            blast_defense_level, \
            combat_level, \
            interaction_mode, \
            minimap_mode, \
            interface_kind, \
            multiple_attribute_mode, \
            minimap_color, \
            language_dll_help, \
            language_dll_hotkey_text, \
            hot_key, \
            recyclable, \
            enable_auto_gather, \
            create_doppelganger_on_death, \
            resource_gather_group, \
            occlusion_mode, \
            obstruction_type, \
            obstruction_class, \
            trait, \
            civilization, \
            nothing, \
            selection_effect, \
            editor_selection_colour, \
            outline_size_x, \
            outline_size_y, \
            outline_size_z, \
            scenario_triggers_1, \
            scenario_triggers_2 = struct.unpack(FORMAT, content.consume_range(FORMAT_LENGTH))

        resource_storages = content.read_class_array_3(ResourceStorage)
        damage_graphic_size = content.read_int_8()
        damage_graphics = content.read_class_array(DamageGraphic, damage_graphic_size)
        selection_sound = content.read_int_16()
        dying_sound = content.read_int_16()
        wwise_train_sound_id = content.read_int_32()
        wwise_damage_sound_id = content.read_int_32()
        wwise_selection_sound_id = content.read_int_32()
        wwise_dying_sound_id = content.read_int_32()
        old_attack_reaction = content.read_int_8()
        convert_terrain = content.read_int_8()
        name = content.read_debug_string()
        copy_id = content.read_int_16()
        base_id = content.read_int_16()
        speed = None
        dead_fish = None
        bird = None
        type_50 = None
        projectile = None
        creatable = None
        building = None
        if type_ != UnitType.AoeTrees:
            if type_ >= UnitType.Flag:
                speed = content.read_float()
                if type_ >= UnitType.DeadFish:
                    dead_fish = content.read_class(DeadFish)
                if type_ >= UnitType.Bird:
                    bird = content.read_class(Bird)
                if type_ >= UnitType.Combatant:
                    type_50 = content.read_class(Type50)
                if type_ == UnitType.Projectile:
                    projectile = content.read_class(Projectile)
                if type_ >= UnitType.Creatable:
                    creatable = content.read_class(Creatable)
                if type_ == UnitType.Building:
                    building = content.read_class(Building)

        if creatable:
            if not creatable.train_locations:
                creatable.train_locations = [TrainLocation(train_time=0, unit_id=-1, button_id=0, hot_key_id=16_000)]
            creatable.train_locations[0].hot_key_id = hot_key

        return cls(
            type=type_,
            id=id_,
            language_dll_name=language_dll_name,
            language_dll_creation=language_dll_creation,
            class_=class_,
            standing_graphic=(standing_graphic_1, standing_graphic_2),
            dying_graphic=dying_graphic,
            undead_graphic=undead_graphic,
            undead_mode=undead_mode,
            hit_points=hit_points,
            line_of_sight=line_of_sight,
            garrison_capacity=garrison_capacity,
            collision_size_x=collision_size_x,
            collision_size_y=collision_size_y,
            collision_size_z=collision_size_z,
            train_sound=train_sound,
            damage_sound=damage_sound,
            dead_unit_id=dead_unit_id,
            blood_unit_id=blood_unit_id,
            sort_number=sort_number,
            can_be_built_on=can_be_built_on,
            icon_id=icon_id,
            hide_in_editor=hide_in_editor,
            old_portrait_pict=old_portrait_pict,
            enabled=enabled,
            disabled=disabled,
            placement_side_terrain=(placement_side_terrain_1, placement_side_terrain_2),
            placement_terrain=(placement_terrain_1, placement_terrain_2),
            clearance_size=(clearance_size_1, clearance_size_2),
            hill_mode=hill_mode,
            fog_visibility=fog_visibility,
            terrain_restriction=terrain_restriction,
            fly_mode=fly_mode,
            resource_capacity=resource_capacity,
            resource_decay=resource_decay,
            blast_defense_level=blast_defense_level,
            combat_level=combat_level,
            interaction_mode=interaction_mode,
            minimap_mode=minimap_mode,
            interface_kind=interface_kind,
            multiple_attribute_mode=multiple_attribute_mode,
            minimap_color=minimap_color,
            language_dll_help=language_dll_help,
            language_dll_hotkey_text=language_dll_hotkey_text,
            hot_key=hot_key,
            recyclable=recyclable,
            enable_auto_gather=enable_auto_gather,
            create_doppelganger_on_death=create_doppelganger_on_death,
            resource_gather_group=resource_gather_group,
            occlusion_mode=occlusion_mode,
            obstruction_type=obstruction_type,
            obstruction_class=obstruction_class,
            trait=trait,
            civilization=civilization,
            nothing=nothing,
            selection_effect=selection_effect,
            editor_selection_colour=editor_selection_colour,
            outline_size_x=outline_size_x,
            outline_size_y=outline_size_y,
            outline_size_z=outline_size_z,
            scenario_triggers_1=scenario_triggers_1,
            scenario_triggers_2=scenario_triggers_2,
            resource_storages=resource_storages,
            damage_graphics=damage_graphics,
            selection_sound=selection_sound,
            dying_sound=dying_sound,
            wwise_train_sound_id=wwise_train_sound_id,
            wwise_damage_sound_id=wwise_damage_sound_id,
            wwise_selection_sound_id=wwise_selection_sound_id,
            wwise_dying_sound_id=wwise_dying_sound_id,
            old_attack_reaction=old_attack_reaction,
            convert_terrain=convert_terrain,
            name=name,
            copy_id=copy_id,
            base_id=base_id,
            speed=speed,
            dead_fish=dead_fish,
            bird=bird,
            type_50=type_50,
            projectile=projectile,
            creatable=creatable,
            building=building,
        )

    @classmethod
    def from_bytes_88(cls, content: ByteHandler) -> 'Unit':
        type_, \
            id_, \
            language_dll_name, \
            language_dll_creation, \
            class_, \
            standing_graphic_1, standing_graphic_2, \
            dying_graphic, \
            undead_graphic, \
            undead_mode, \
            hit_points, \
            line_of_sight, \
            garrison_capacity, \
            collision_size_x, \
            collision_size_y, \
            collision_size_z, \
            train_sound, \
            damage_sound, \
            dead_unit_id, \
            blood_unit_id, \
            sort_number, \
            can_be_built_on, \
            icon_id, \
            hide_in_editor, \
            old_portrait_pict, \
            enabled, \
            disabled, \
            placement_side_terrain_1, placement_side_terrain_2, \
            placement_terrain_1, placement_terrain_2, \
            clearance_size_1, clearance_size_2, \
            hill_mode, \
            fog_visibility, \
            terrain_restriction, \
            fly_mode, \
            resource_capacity, \
            resource_decay, \
            blast_defense_level, \
            combat_level, \
            interaction_mode, \
            minimap_mode, \
            interface_kind, \
            multiple_attribute_mode, \
            minimap_color, \
            language_dll_help, \
            language_dll_hotkey_text, \
            recyclable, \
            enable_auto_gather, \
            create_doppelganger_on_death, \
            resource_gather_group, \
            occlusion_mode, \
            obstruction_type, \
            obstruction_class, \
            trait, \
            civilization, \
            nothing, \
            selection_effect, \
            editor_selection_colour, \
            outline_size_x, \
            outline_size_y, \
            outline_size_z, \
            scenario_triggers_1, \
            scenario_triggers_2 = struct.unpack(FORMAT_88, content.consume_range(FORMAT_LENGTH_88))

        hot_key = 16_000
        resource_storages = content.read_class_array_3(ResourceStorage)
        damage_graphic_size = content.read_int_8()
        damage_graphics = content.read_class_array(DamageGraphic, damage_graphic_size)
        selection_sound = content.read_int_16()
        dying_sound = content.read_int_16()
        wwise_train_sound_id = content.read_int_32()
        wwise_damage_sound_id = content.read_int_32()
        wwise_selection_sound_id = content.read_int_32()
        wwise_dying_sound_id = content.read_int_32()
        old_attack_reaction = content.read_int_8()
        convert_terrain = content.read_int_8()
        name = content.read_debug_string()
        copy_id = content.read_int_16()
        base_id = content.read_int_16()
        speed = None
        dead_fish = None
        bird = None
        type_50 = None
        projectile = None
        creatable = None
        building = None
        if type_ != UnitType.AoeTrees:
            if type_ >= UnitType.Flag:
                speed = content.read_float()
                if type_ >= UnitType.DeadFish:
                    dead_fish = content.read_class(DeadFish)
                if type_ >= UnitType.Bird:
                    bird = content.read_class(Bird)
                if type_ >= UnitType.Combatant:
                    type_50 = content.read_class(Type50)
                if type_ == UnitType.Projectile:
                    projectile = content.read_class(Projectile)
                if type_ >= UnitType.Creatable:
                    creatable = content.read_class(Creatable)
                if type_ == UnitType.Building:
                    building = content.read_class(Building)
        if creatable and creatable.train_locations:
            hot_key = creatable.train_locations[0].hot_key_id

        return cls(
            type=type_,
            id=id_,
            language_dll_name=language_dll_name,
            language_dll_creation=language_dll_creation,
            class_=class_,
            standing_graphic=(standing_graphic_1, standing_graphic_2),
            dying_graphic=dying_graphic,
            undead_graphic=undead_graphic,
            undead_mode=undead_mode,
            hit_points=hit_points,
            line_of_sight=line_of_sight,
            garrison_capacity=garrison_capacity,
            collision_size_x=collision_size_x,
            collision_size_y=collision_size_y,
            collision_size_z=collision_size_z,
            train_sound=train_sound,
            damage_sound=damage_sound,
            dead_unit_id=dead_unit_id,
            blood_unit_id=blood_unit_id,
            sort_number=sort_number,
            can_be_built_on=can_be_built_on,
            icon_id=icon_id,
            hide_in_editor=hide_in_editor,
            old_portrait_pict=old_portrait_pict,
            enabled=enabled,
            disabled=disabled,
            placement_side_terrain=(placement_side_terrain_1, placement_side_terrain_2),
            placement_terrain=(placement_terrain_1, placement_terrain_2),
            clearance_size=(clearance_size_1, clearance_size_2),
            hill_mode=hill_mode,
            fog_visibility=fog_visibility,
            terrain_restriction=terrain_restriction,
            fly_mode=fly_mode,
            resource_capacity=resource_capacity,
            resource_decay=resource_decay,
            blast_defense_level=blast_defense_level,
            combat_level=combat_level,
            interaction_mode=interaction_mode,
            minimap_mode=minimap_mode,
            interface_kind=interface_kind,
            multiple_attribute_mode=multiple_attribute_mode,
            minimap_color=minimap_color,
            language_dll_help=language_dll_help,
            language_dll_hotkey_text=language_dll_hotkey_text,
            hot_key=hot_key,
            recyclable=recyclable,
            enable_auto_gather=enable_auto_gather,
            create_doppelganger_on_death=create_doppelganger_on_death,
            resource_gather_group=resource_gather_group,
            occlusion_mode=occlusion_mode,
            obstruction_type=obstruction_type,
            obstruction_class=obstruction_class,
            trait=trait,
            civilization=civilization,
            nothing=nothing,
            selection_effect=selection_effect,
            editor_selection_colour=editor_selection_colour,
            outline_size_x=outline_size_x,
            outline_size_y=outline_size_y,
            outline_size_z=outline_size_z,
            scenario_triggers_1=scenario_triggers_1,
            scenario_triggers_2=scenario_triggers_2,
            resource_storages=resource_storages,
            damage_graphics=damage_graphics,
            selection_sound=selection_sound,
            dying_sound=dying_sound,
            wwise_train_sound_id=wwise_train_sound_id,
            wwise_damage_sound_id=wwise_damage_sound_id,
            wwise_selection_sound_id=wwise_selection_sound_id,
            wwise_dying_sound_id=wwise_dying_sound_id,
            old_attack_reaction=old_attack_reaction,
            convert_terrain=convert_terrain,
            name=name,
            copy_id=copy_id,
            base_id=base_id,
            speed=speed,
            dead_fish=dead_fish,
            bird=bird,
            type_50=type_50,
            projectile=projectile,
            creatable=creatable,
            building=building,
        )

    def to_bytes(self, version: Version) -> bytes:
        if version >= Version.VER_88:
            return self.to_bytes_88(version)
        return self.to_bytes_84(version)

    def to_bytes_84(self, version: Version) -> bytes:
        speed = b''
        dead_fish = b''
        bird = b''
        type_50 = b''
        projectile = b''
        creatable = b''
        building = b''
        if self.type != UnitType.AoeTrees:
            if self.type >= UnitType.Flag:
                speed = self.write_float(self.speed) if self.speed is not None else b''
                if self.type >= UnitType.DeadFish:
                    dead_fish = self.write_class(self.dead_fish, version) if self.dead_fish is not None else b''
                if self.type >= UnitType.Bird:
                    bird = self.write_class(self.bird, version) if self.bird is not None else b''
                if self.type >= UnitType.Combatant:
                    type_50 = self.write_class(self.type_50, version) if self.type_50 is not None else b''
                if self.type == UnitType.Projectile:
                    projectile = self.write_class(self.projectile, version) if self.projectile is not None else b''
                if self.type >= UnitType.Creatable:
                    creatable = self.write_class(self.creatable, version) if self.creatable is not None else b''
                if self.type == UnitType.Building:
                    building = self.write_class(self.building, version) if self.building is not None else b''
        return struct.pack(FORMAT,
                           self.type,
                           self.id,
                           self.language_dll_name,
                           self.language_dll_creation,
                           self.class_,
                           *self.standing_graphic,
                           self.dying_graphic,
                           self.undead_graphic,
                           self.undead_mode,
                           self.hit_points,
                           self.line_of_sight,
                           self.garrison_capacity,
                           self.collision_size_x,
                           self.collision_size_y,
                           self.collision_size_z,
                           self.train_sound,
                           self.damage_sound,
                           self.dead_unit_id,
                           self.blood_unit_id,
                           self.sort_number,
                           self.can_be_built_on,
                           self.icon_id,
                           self.hide_in_editor,
                           self.old_portrait_pict,
                           self.enabled,
                           self.disabled,
                           *self.placement_side_terrain,
                           *self.placement_terrain,
                           *self.clearance_size,
                           self.hill_mode,
                           self.fog_visibility,
                           self.terrain_restriction,
                           self.fly_mode,
                           self.resource_capacity,
                           self.resource_decay,
                           self.blast_defense_level,
                           self.combat_level,
                           self.interaction_mode,
                           self.minimap_mode,
                           self.interface_kind,
                           self.multiple_attribute_mode,
                           self.minimap_color,
                           self.language_dll_help,
                           self.language_dll_hotkey_text,
                           self.hot_key,
                           self.recyclable,
                           self.enable_auto_gather,
                           self.create_doppelganger_on_death,
                           self.resource_gather_group,
                           self.occlusion_mode,
                           self.obstruction_type,
                           self.obstruction_class,
                           self.trait,
                           self.civilization,
                           self.nothing,
                           self.selection_effect,
                           self.editor_selection_colour,
                           self.outline_size_x,
                           self.outline_size_y,
                           self.outline_size_z,
                           self.scenario_triggers_1,
                           self.scenario_triggers_2,
                           ) + b''.join([
            self.write_class_array(self.resource_storages, version),
            self.write_int_8(len(self.damage_graphics)),
            self.write_class_array(self.damage_graphics, version),
            self.write_int_16(self.selection_sound),
            self.write_int_16(self.dying_sound),
            self.write_int_32(self.wwise_train_sound_id),
            self.write_int_32(self.wwise_damage_sound_id),
            self.write_int_32(self.wwise_selection_sound_id),
            self.write_int_32(self.wwise_dying_sound_id),
            self.write_int_8(self.old_attack_reaction),
            self.write_int_8(self.convert_terrain),
            self.write_debug_string(self.name),
            self.write_int_16(self.copy_id),
            self.write_int_16(self.base_id),
            speed,
            dead_fish,
            bird,
            type_50,
            projectile,
            creatable,
            building,
        ])

    def to_bytes_88(self, version: Version) -> bytes:
        speed = b''
        dead_fish = b''
        bird = b''
        type_50 = b''
        projectile = b''
        creatable = b''
        building = b''
        if self.type != UnitType.AoeTrees:
            if self.type >= UnitType.Flag:
                speed = self.write_float(self.speed) if self.speed is not None else b''
                if self.type >= UnitType.DeadFish:
                    dead_fish = self.write_class(self.dead_fish, version) if self.dead_fish is not None else b''
                if self.type >= UnitType.Bird:
                    bird = self.write_class(self.bird, version) if self.bird is not None else b''
                if self.type >= UnitType.Combatant:
                    type_50 = self.write_class(self.type_50, version) if self.type_50 is not None else b''
                if self.type == UnitType.Projectile:
                    projectile = self.write_class(self.projectile, version) if self.projectile is not None else b''
                if self.type >= UnitType.Creatable:
                    creatable = self.write_class(self.creatable, version) if self.creatable is not None else b''
                if self.type == UnitType.Building:
                    building = self.write_class(self.building, version) if self.building is not None else b''
        return struct.pack(FORMAT_88,
                           self.type,
                           self.id,
                           self.language_dll_name,
                           self.language_dll_creation,
                           self.class_,
                           *self.standing_graphic,
                           self.dying_graphic,
                           self.undead_graphic,
                           self.undead_mode,
                           self.hit_points,
                           self.line_of_sight,
                           self.garrison_capacity,
                           self.collision_size_x,
                           self.collision_size_y,
                           self.collision_size_z,
                           self.train_sound,
                           self.damage_sound,
                           self.dead_unit_id,
                           self.blood_unit_id,
                           self.sort_number,
                           self.can_be_built_on,
                           self.icon_id,
                           self.hide_in_editor,
                           self.old_portrait_pict,
                           self.enabled,
                           self.disabled,
                           *self.placement_side_terrain,
                           *self.placement_terrain,
                           *self.clearance_size,
                           self.hill_mode,
                           self.fog_visibility,
                           self.terrain_restriction,
                           self.fly_mode,
                           self.resource_capacity,
                           self.resource_decay,
                           self.blast_defense_level,
                           self.combat_level,
                           self.interaction_mode,
                           self.minimap_mode,
                           self.interface_kind,
                           self.multiple_attribute_mode,
                           self.minimap_color,
                           self.language_dll_help,
                           self.language_dll_hotkey_text,
                           self.recyclable,
                           self.enable_auto_gather,
                           self.create_doppelganger_on_death,
                           self.resource_gather_group,
                           self.occlusion_mode,
                           self.obstruction_type,
                           self.obstruction_class,
                           self.trait,
                           self.civilization,
                           self.nothing,
                           self.selection_effect,
                           self.editor_selection_colour,
                           self.outline_size_x,
                           self.outline_size_y,
                           self.outline_size_z,
                           self.scenario_triggers_1,
                           self.scenario_triggers_2,
                           ) + b''.join([
            self.write_class_array(self.resource_storages, version),
            self.write_int_8(len(self.damage_graphics)),
            self.write_class_array(self.damage_graphics, version),
            self.write_int_16(self.selection_sound),
            self.write_int_16(self.dying_sound),
            self.write_int_32(self.wwise_train_sound_id),
            self.write_int_32(self.wwise_damage_sound_id),
            self.write_int_32(self.wwise_selection_sound_id),
            self.write_int_32(self.wwise_dying_sound_id),
            self.write_int_8(self.old_attack_reaction),
            self.write_int_8(self.convert_terrain),
            self.write_debug_string(self.name),
            self.write_int_16(self.copy_id),
            self.write_int_16(self.base_id),
            speed,
            dead_fish,
            bird,
            type_50,
            projectile,
            creatable,
            building,
        ])
