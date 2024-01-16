from dataclasses import dataclass

from src.bird import Bird
from src.building import Building
from src.common import ByteHandler, UnitType
from src.creatable import Creatable
from src.damagegraphic import DamageGraphic
from src.deadfish import DeadFish
from src.projectile import Projectile
from src.resourcestorage import ResourceStorage
from src.type50 import Type50


@dataclass
class Unit(ByteHandler):
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

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.type = self.read_int_8()
        self.id = self.read_int_16()
        self.language_dll_name = self.read_int_32()
        self.language_dll_creation = self.read_int_32()
        self.class_ = self.read_int_16()
        self.standing_graphic = self.read_int_16_array(2)
        self.dying_graphic = self.read_int_16()
        self.undead_graphic = self.read_int_16()
        self.undead_mode = self.read_int_8()
        self.hit_points = self.read_int_16()
        self.line_of_sight = self.read_float()
        self.garrison_capacity = self.read_int_8()
        self.collision_size_x = self.read_float()
        self.collision_size_y = self.read_float()
        self.collision_size_z = self.read_float()
        self.train_sound = self.read_int_16()
        self.damage_sound = self.read_int_16()
        self.dead_unit_id = self.read_int_16()
        self.blood_unit_id = self.read_int_16()
        self.sort_number = self.read_int_8()
        self.can_be_built_on = self.read_int_8()
        self.icon_id = self.read_int_16()
        self.hide_in_editor = self.read_int_8()
        self.old_portrait_pict = self.read_int_16()
        self.enabled = self.read_int_8()
        self.disabled = self.read_int_8()
        self.placement_side_terrain = self.read_int_16_array(2)
        self.placement_terrain = self.read_int_16_array(2)
        self.clearance_size = self.read_float_array(2)
        self.hill_mode = self.read_int_8()
        self.fog_visibility = self.read_int_8()
        self.terrain_restriction = self.read_int_16()
        self.fly_mode = self.read_int_8()
        self.resource_capacity = self.read_int_16()
        self.resource_decay = self.read_float()
        self.blast_defense_level = self.read_int_8()
        self.combat_level = self.read_int_8()
        self.interation_mode = self.read_int_8()
        self.minimap_mode = self.read_int_8()
        self.interface_kind = self.read_int_8()
        self.multiple_attribute_mode = self.read_float()
        self.minimap_color = self.read_int_8()
        self.language_dll_help = self.read_int_32()
        self.language_dll_hotkey_text = self.read_int_32()
        self.hot_key = self.read_int_32()
        self.recyclable = self.read_int_8()
        self.enable_auto_gather = self.read_int_8()
        self.create_doppelganger_on_death = self.read_int_8()
        self.resource_gather_group = self.read_int_8()
        self.occlusion_mode = self.read_int_8()
        self.obstruction_type = self.read_int_8()
        self.obstruction_class = self.read_int_8()
        self.trait = self.read_int_8()
        self.civilization = self.read_int_8()
        self.nothing = self.read_int_16()
        self.selection_effect = self.read_int_8()
        self.editor_selection_colour = self.read_int_8()
        self.outline_size_x = self.read_float()
        self.outline_size_y = self.read_float()
        self.outline_size_z = self.read_float()
        self.scenario_triggers_1 = self.read_int_32()
        self.scenario_triggers_2 = self.read_int_32()
        self.resource_storages = self.read_resource_storage_array(3)
        self.damage_graphic_size = self.read_int_8()
        self.damage_graphics = self.read_damage_graphic_array(self.damage_graphic_size)
        self.selection_sound = self.read_int_16()
        self.dying_sound = self.read_int_16()
        self.wwise_train_sound_id = self.read_int_32()
        self.wwise_damage_sound_id = self.read_int_32()
        self.wwise_selection_sound_id = self.read_int_32()
        self.wwise_dying_sound_id = self.read_int_32()
        self.old_attack_reaction = self.read_int_8()
        self.convert_terrain = self.read_int_8()
        self.name = self.read_debug_string()
        self.copy_id = self.read_int_16()
        self.base_id = self.read_int_16()
        if self.type == UnitType.AoeTrees:
            return
        if self.type >= UnitType.Flag:
            self.speed = self.read_float()
        else:
            return
        if self.type >= UnitType.DeadFish:
            self.dead_fish = self.read_dead_fish()
        if self.type >= UnitType.Bird:
            self.bird = self.read_bird()
        if self.type >= UnitType.Combatant:
            self.type_50 = self.read_type_50()
        if self.type == UnitType.Projectile:
            self.projectile = self.read_projectile()
        if self.type >= UnitType.Creatable:
            self.creatable = self.read_creatable()
        if self.type == UnitType.Building:
            self.building = self.read_building()

    def read_resource_storage_array(self, size: int) -> list[ResourceStorage]:
        elements = []
        for i in range(size):
            resource_storage = ResourceStorage(self.content[self.offset:])
            elements.append(resource_storage)
            self.offset += resource_storage.offset
        return elements

    def read_damage_graphic_array(self, size: int) -> list[DamageGraphic]:
        elements = []
        for i in range(size):
            damage_graphic = DamageGraphic(self.content[self.offset:])
            elements.append(damage_graphic)
            self.offset += damage_graphic.offset
        return elements

    def read_dead_fish(self) -> DeadFish:
        dead_fish = DeadFish(self.content[self.offset:])
        self.offset += dead_fish.offset
        return dead_fish

    def read_bird(self) -> Bird:
        bird = Bird(self.content[self.offset:])
        self.offset += bird.offset
        return bird

    def read_type_50(self) -> Type50:
        type_50 = Type50(self.content[self.offset:])
        self.offset += type_50.offset
        return type_50

    def read_projectile(self) -> Projectile:
        projectile = Projectile(self.content[self.offset:])
        self.offset += projectile.offset
        return projectile

    def read_creatable(self) -> Creatable:
        creatable = Creatable(self.content[self.offset:])
        self.offset += creatable.offset
        return creatable

    def read_building(self) -> Building:
        building = Building(self.content[self.offset:])
        self.offset += building.offset
        return building
