from dataclasses import dataclass

from src.common import ByteHandler


@dataclass
class Task(ByteHandler):
    task_type: int
    id: int
    is_default: int
    action_type: int
    class_id: int
    unit_id: int
    terrain_id: int
    resource_in: int
    resource_multiplier: int
    resource_out: int
    unused_resource: int
    work_value_1: float
    work_value_2: float
    work_range: float
    auto_search_targets: int
    search_wait_time: float
    enable_targeting: int
    combat_level_flag: int
    gather_type: int
    work_flag_2: int
    target_diplomacy: int
    carry_check: int
    pick_for_construction: int
    moving_graphic_id: int
    proceeding_graphic_id: int
    working_graphic_id: int
    carrying_graphic_id: int
    resource_gathering_sound_id: int
    resource_deposit_sound_id: int
    wwise_resource_gathering_sound_id: int
    wwise_resource_deposit_sound_id: int

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.task_type = self.read_int_16()
        self.id = self.read_int_16()
        self.is_default = self.read_int_8()
        self.action_type = self.read_int_16()
        self.class_id = self.read_int_16()
        self.unit_id = self.read_int_16()
        self.terrain_id = self.read_int_16()
        self.resource_in = self.read_int_16()
        self.resource_multiplier = self.read_int_16()
        self.resource_out = self.read_int_16()
        self.unused_resource = self.read_int_16()
        self.work_value_1 = self.read_float()
        self.work_value_2 = self.read_float()
        self.work_range = self.read_float()
        self.auto_search_targets = self.read_int_8()
        self.search_wait_time = self.read_float()
        self.enable_targeting = self.read_int_8()
        self.combat_level_flag = self.read_int_8()
        self.gather_type = self.read_int_16()
        self.work_flag_2 = self.read_int_16()
        self.target_diplomacy = self.read_int_8()
        self.carry_check = self.read_int_8()
        self.pick_for_construction = self.read_int_8()
        self.moving_graphic_id = self.read_int_16()
        self.proceeding_graphic_id = self.read_int_16()
        self.working_graphic_id = self.read_int_16()
        self.carrying_graphic_id = self.read_int_16()
        self.resource_gathering_sound_id = self.read_int_16()
        self.resource_deposit_sound_id = self.read_int_16()
        self.wwise_resource_gathering_sound_id = self.read_int_32()
        self.wwise_resource_deposit_sound_id = self.read_int_32()
