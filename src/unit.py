import typing
from dataclasses import dataclass

from src.bird import Bird
from src.building import Building
from src.common import ByteHandler, UnitType, GenieClass
from src.creatable import Creatable
from src.damagegraphic import DamageGraphic
from src.deadfish import DeadFish
from src.projectile import Projectile
from src.resourcestorage import ResourceStorage
from src.type50 import Type50


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
        type = content.read_int_8()
        id = content.read_int_16()
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
        if type != UnitType.AoeTrees:
            if type >= UnitType.Flag:
                speed = content.read_float()
                if type >= UnitType.DeadFish:
                    dead_fish = content.read_class(DeadFish)
                if type >= UnitType.Bird:
                    bird = content.read_class(Bird)
                if type >= UnitType.Combatant:
                    type_50 = content.read_class(Type50)
                if type == UnitType.Projectile:
                    projectile = content.read_class(Projectile)
                if type >= UnitType.Creatable:
                    creatable = content.read_class(Creatable)
                if type == UnitType.Building:
                    building = content.read_class(Building)

        return cls(
            type=type,
            id=id,
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
