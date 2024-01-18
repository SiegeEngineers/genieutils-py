from dataclasses import dataclass

from genieutils.common import ByteHandler, UnitType, GenieClass
from genieutils.task import Task


@dataclass
class ResourceStorage(GenieClass):
    type: int
    amount: float
    flag: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'ResourceStorage':
        return cls(
            type=content.read_int_16(),
            amount=content.read_float(),
            flag=content.read_int_8(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.type),
            self.write_float(self.amount),
            self.write_int_8(self.flag),
        ])


@dataclass
class DamageGraphic(GenieClass):
    graphic_id: int
    damage_percent: int
    apply_mode: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'DamageGraphic':
        return cls(
            graphic_id=content.read_int_16(),
            damage_percent=content.read_int_16(),
            apply_mode=content.read_int_8(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.graphic_id),
            self.write_int_16(self.damage_percent),
            self.write_int_8(self.apply_mode),
        ])


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

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.walking_graphic),
            self.write_int_16(self.running_graphic),
            self.write_float(self.rotation_speed),
            self.write_int_8(self.old_size_class),
            self.write_int_16(self.tracking_unit),
            self.write_int_8(self.tracking_unit_mode),
            self.write_float(self.tracking_unit_density),
            self.write_int_8(self.old_move_algorithm),
            self.write_float(self.turn_radius),
            self.write_float(self.turn_radius_speed),
            self.write_float(self.max_yaw_per_second_moving),
            self.write_float(self.stationary_yaw_revolution_time),
            self.write_float(self.max_yaw_per_second_stationary),
            self.write_float(self.min_collision_size_multiplier),
        ])


@dataclass
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
    task_size: int
    tasks: list[Task]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Bird':
        default_task_id = content.read_int_16()
        search_radius = content.read_float()
        work_rate = content.read_float()
        drop_sites = content.read_int_16_array(3)
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
            task_size=task_size,
            tasks=tasks,
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.default_task_id),
            self.write_float(self.search_radius),
            self.write_float(self.work_rate),
            self.write_int_16_array(self.drop_sites),
            self.write_int_8(self.task_swap_group),
            self.write_int_16(self.attack_sound),
            self.write_int_16(self.move_sound),
            self.write_int_32(self.wwise_attack_sound_id),
            self.write_int_32(self.wwise_move_sound_id),
            self.write_int_8(self.run_pattern),
            self.write_int_16(self.task_size),
            self.write_class_array(self.tasks),
        ])


@dataclass
class AttackOrArmor(GenieClass):
    class_: int
    amount: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'AttackOrArmor':
        return cls(
            class_=content.read_int_16(),
            amount=content.read_int_16(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.class_),
            self.write_int_16(self.amount),
        ])


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

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.base_armor),
            self.write_int_16(self.attack_count),
            self.write_class_array(self.attacks),
            self.write_int_16(self.armour_count),
            self.write_class_array(self.armours),
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


@dataclass
class Projectile(GenieClass):
    projectile_type: int
    smart_mode: int
    hit_mode: int
    vanish_mode: int
    area_effect_specials: int
    projectile_arc: float

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Projectile':
        return cls(
            projectile_type=content.read_int_8(),
            smart_mode=content.read_int_8(),
            hit_mode=content.read_int_8(),
            vanish_mode=content.read_int_8(),
            area_effect_specials=content.read_int_8(),
            projectile_arc=content.read_float(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_8(self.projectile_type),
            self.write_int_8(self.smart_mode),
            self.write_int_8(self.hit_mode),
            self.write_int_8(self.vanish_mode),
            self.write_int_8(self.area_effect_specials),
            self.write_float(self.projectile_arc),
        ])


@dataclass
class ResourceCost(GenieClass):
    type: int
    amount: int
    flag: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'ResourceCost':
        return cls(
            type=content.read_int_16(),
            amount=content.read_int_16(),
            flag=content.read_int_16(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.type),
            self.write_int_16(self.amount),
            self.write_int_16(self.flag),
        ])


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

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_class_array(self.resource_costs),
            self.write_int_16(self.train_time),
            self.write_int_16(self.train_location_id),
            self.write_int_8(self.button_id),
            self.write_float(self.rear_attack_modifier),
            self.write_float(self.flank_attack_modifier),
            self.write_int_8(self.creatable_type),
            self.write_int_8(self.hero_mode),
            self.write_int_32(self.garrison_graphic),
            self.write_int_16(self.spawning_graphic),
            self.write_int_16(self.upgrade_graphic),
            self.write_int_16(self.hero_glow_graphic),
            self.write_float(self.max_charge),
            self.write_float(self.recharge_rate),
            self.write_int_16(self.charge_event),
            self.write_int_16(self.charge_type),
            self.write_float(self.min_conversion_time_mod),
            self.write_float(self.max_conversion_time_mod),
            self.write_float(self.conversion_chance_mod),
            self.write_float(self.total_projectiles),
            self.write_int_8(self.max_total_projectiles),
            self.write_float_array(self.projectile_spawning_area),
            self.write_int_32(self.secondary_projectile_unit),
            self.write_int_32(self.special_graphic),
            self.write_int_8(self.special_ability),
            self.write_int_16(self.displayed_pierce_armor),
        ])


@dataclass
class BuildingAnnex(GenieClass):
    unit_id: int
    misplacement_x: float
    misplacement_y: float

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'BuildingAnnex':
        return cls(
            unit_id=content.read_int_16(),
            misplacement_x=content.read_float(),
            misplacement_y=content.read_float(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.unit_id),
            self.write_float(self.misplacement_x),
            self.write_float(self.misplacement_y),
        ])


@dataclass
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
    annexes: list[BuildingAnnex]
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
    looting_table: list[int]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Building':
        return cls(
            construction_graphic_id=content.read_int_16(),
            snow_graphic_id=content.read_int_16(),
            destruction_graphic_id=content.read_int_16(),
            destruction_rubble_graphic_id=content.read_int_16(),
            researching_graphic=content.read_int_16(),
            research_completed_graphic=content.read_int_16(),
            adjacent_mode=content.read_int_8(),
            graphics_angle=content.read_int_16(),
            disappears_when_built=content.read_int_8(),
            stack_unit_id=content.read_int_16(),
            foundation_terrain_id=content.read_int_16(),
            old_overlap_id=content.read_int_16(),
            tech_id=content.read_int_16(),
            can_burn=content.read_int_8(),
            annexes=content.read_class_array(BuildingAnnex, 4),
            head_unit=content.read_int_16(),
            transform_unit=content.read_int_16(),
            transform_sound=content.read_int_16(),
            construction_sound=content.read_int_16(),
            wwise_transform_sound_id=content.read_int_32(),
            wwise_construction_sound_id=content.read_int_32(),
            garrison_type=content.read_int_8(),
            garrison_heal_rate=content.read_float(),
            garrison_repair_rate=content.read_float(),
            pile_unit=content.read_int_16(),
            looting_table=content.read_int_8_array(6),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.construction_graphic_id),
            self.write_int_16(self.snow_graphic_id),
            self.write_int_16(self.destruction_graphic_id),
            self.write_int_16(self.destruction_rubble_graphic_id),
            self.write_int_16(self.researching_graphic),
            self.write_int_16(self.research_completed_graphic),
            self.write_int_8(self.adjacent_mode),
            self.write_int_16(self.graphics_angle),
            self.write_int_8(self.disappears_when_built),
            self.write_int_16(self.stack_unit_id),
            self.write_int_16(self.foundation_terrain_id),
            self.write_int_16(self.old_overlap_id),
            self.write_int_16(self.tech_id),
            self.write_int_8(self.can_burn),
            self.write_class_array(self.annexes),
            self.write_int_16(self.head_unit),
            self.write_int_16(self.transform_unit),
            self.write_int_16(self.transform_sound),
            self.write_int_16(self.construction_sound),
            self.write_int_32(self.wwise_transform_sound_id),
            self.write_int_32(self.wwise_construction_sound_id),
            self.write_int_8(self.garrison_type),
            self.write_float(self.garrison_heal_rate),
            self.write_float(self.garrison_repair_rate),
            self.write_int_16(self.pile_unit),
            self.write_int_8_array(self.looting_table),
        ])


@dataclass
class Unit(GenieClass):
    type: int
    id: int
    language_dll_name: int
    language_dll_creation: int
    class_: int
    standing_graphic: list[int]
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
    placement_side_terrain: list[int]
    placement_terrain: list[int]
    clearance_size: list[float]
    hill_mode: int
    fog_visibility: int
    terrain_restriction: int
    fly_mode: int
    resource_capacity: int
    resource_decay: float
    blast_defense_level: int
    combat_level: int
    interation_mode: int
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
    resource_storages: list[ResourceStorage]
    damage_graphic_size: int
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
        type_ = content.read_int_8()
        id_ = content.read_int_16()
        language_dll_name = content.read_int_32()
        language_dll_creation = content.read_int_32()
        class_ = content.read_int_16()
        standing_graphic = content.read_int_16_array(2)
        dying_graphic = content.read_int_16()
        undead_graphic = content.read_int_16()
        undead_mode = content.read_int_8()
        hit_points = content.read_int_16()
        line_of_sight = content.read_float()
        garrison_capacity = content.read_int_8()
        collision_size_x = content.read_float()
        collision_size_y = content.read_float()
        collision_size_z = content.read_float()
        train_sound = content.read_int_16()
        damage_sound = content.read_int_16()
        dead_unit_id = content.read_int_16()
        blood_unit_id = content.read_int_16()
        sort_number = content.read_int_8()
        can_be_built_on = content.read_int_8()
        icon_id = content.read_int_16()
        hide_in_editor = content.read_int_8()
        old_portrait_pict = content.read_int_16()
        enabled = content.read_int_8()
        disabled = content.read_int_8()
        placement_side_terrain = content.read_int_16_array(2)
        placement_terrain = content.read_int_16_array(2)
        clearance_size = content.read_float_array(2)
        hill_mode = content.read_int_8()
        fog_visibility = content.read_int_8()
        terrain_restriction = content.read_int_16()
        fly_mode = content.read_int_8()
        resource_capacity = content.read_int_16()
        resource_decay = content.read_float()
        blast_defense_level = content.read_int_8()
        combat_level = content.read_int_8()
        interation_mode = content.read_int_8()
        minimap_mode = content.read_int_8()
        interface_kind = content.read_int_8()
        multiple_attribute_mode = content.read_float()
        minimap_color = content.read_int_8()
        language_dll_help = content.read_int_32()
        language_dll_hotkey_text = content.read_int_32()
        hot_key = content.read_int_32()
        recyclable = content.read_int_8()
        enable_auto_gather = content.read_int_8()
        create_doppelganger_on_death = content.read_int_8()
        resource_gather_group = content.read_int_8()
        occlusion_mode = content.read_int_8()
        obstruction_type = content.read_int_8()
        obstruction_class = content.read_int_8()
        trait = content.read_int_8()
        civilization = content.read_int_8()
        nothing = content.read_int_16()
        selection_effect = content.read_int_8()
        editor_selection_colour = content.read_int_8()
        outline_size_x = content.read_float()
        outline_size_y = content.read_float()
        outline_size_z = content.read_float()
        scenario_triggers_1 = content.read_int_32()
        scenario_triggers_2 = content.read_int_32()
        resource_storages = content.read_class_array(ResourceStorage, 3)
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

        return cls(
            type=type_,
            id=id_,
            language_dll_name=language_dll_name,
            language_dll_creation=language_dll_creation,
            class_=class_,
            standing_graphic=standing_graphic,
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
            placement_side_terrain=placement_side_terrain,
            placement_terrain=placement_terrain,
            clearance_size=clearance_size,
            hill_mode=hill_mode,
            fog_visibility=fog_visibility,
            terrain_restriction=terrain_restriction,
            fly_mode=fly_mode,
            resource_capacity=resource_capacity,
            resource_decay=resource_decay,
            blast_defense_level=blast_defense_level,
            combat_level=combat_level,
            interation_mode=interation_mode,
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
            damage_graphic_size=damage_graphic_size,
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

    def to_bytes(self) -> bytes:
        speed = b''
        dead_fish = b''
        bird = b''
        type_50 = b''
        projectile = b''
        creatable = b''
        building = b''
        if self.type != UnitType.AoeTrees:
            if self.type >= UnitType.Flag:
                speed = self.write_float(self.speed)
                if self.type >= UnitType.DeadFish:
                    dead_fish = self.write_class(self.dead_fish)
                if self.type >= UnitType.Bird:
                    bird = self.write_class(self.bird)
                if self.type >= UnitType.Combatant:
                    type_50 = self.write_class(self.type_50)
                if self.type == UnitType.Projectile:
                    projectile = self.write_class(self.projectile)
                if self.type >= UnitType.Creatable:
                    creatable = self.write_class(self.creatable)
                if self.type == UnitType.Building:
                    building = self.write_class(self.building)
        return b''.join([
            self.write_int_8(self.type),
            self.write_int_16(self.id),
            self.write_int_32(self.language_dll_name),
            self.write_int_32(self.language_dll_creation),
            self.write_int_16(self.class_),
            self.write_int_16_array(self.standing_graphic),
            self.write_int_16(self.dying_graphic),
            self.write_int_16(self.undead_graphic),
            self.write_int_8(self.undead_mode),
            self.write_int_16(self.hit_points),
            self.write_float(self.line_of_sight),
            self.write_int_8(self.garrison_capacity),
            self.write_float(self.collision_size_x),
            self.write_float(self.collision_size_y),
            self.write_float(self.collision_size_z),
            self.write_int_16(self.train_sound),
            self.write_int_16(self.damage_sound),
            self.write_int_16(self.dead_unit_id),
            self.write_int_16(self.blood_unit_id),
            self.write_int_8(self.sort_number),
            self.write_int_8(self.can_be_built_on),
            self.write_int_16(self.icon_id),
            self.write_int_8(self.hide_in_editor),
            self.write_int_16(self.old_portrait_pict),
            self.write_int_8(self.enabled),
            self.write_int_8(self.disabled),
            self.write_int_16_array(self.placement_side_terrain),
            self.write_int_16_array(self.placement_terrain),
            self.write_float_array(self.clearance_size),
            self.write_int_8(self.hill_mode),
            self.write_int_8(self.fog_visibility),
            self.write_int_16(self.terrain_restriction),
            self.write_int_8(self.fly_mode),
            self.write_int_16(self.resource_capacity),
            self.write_float(self.resource_decay),
            self.write_int_8(self.blast_defense_level),
            self.write_int_8(self.combat_level),
            self.write_int_8(self.interation_mode),
            self.write_int_8(self.minimap_mode),
            self.write_int_8(self.interface_kind),
            self.write_float(self.multiple_attribute_mode),
            self.write_int_8(self.minimap_color),
            self.write_int_32(self.language_dll_help),
            self.write_int_32(self.language_dll_hotkey_text),
            self.write_int_32(self.hot_key),
            self.write_int_8(self.recyclable),
            self.write_int_8(self.enable_auto_gather),
            self.write_int_8(self.create_doppelganger_on_death),
            self.write_int_8(self.resource_gather_group),
            self.write_int_8(self.occlusion_mode),
            self.write_int_8(self.obstruction_type),
            self.write_int_8(self.obstruction_class),
            self.write_int_8(self.trait),
            self.write_int_8(self.civilization),
            self.write_int_16(self.nothing),
            self.write_int_8(self.selection_effect),
            self.write_int_8(self.editor_selection_colour),
            self.write_float(self.outline_size_x),
            self.write_float(self.outline_size_y),
            self.write_float(self.outline_size_z),
            self.write_int_32(self.scenario_triggers_1),
            self.write_int_32(self.scenario_triggers_2),
            self.write_class_array(self.resource_storages),
            self.write_int_8(self.damage_graphic_size),
            self.write_class_array(self.damage_graphics),
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
