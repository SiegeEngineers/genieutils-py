from dataclasses import dataclass

from genieutils.common import ByteHandler, GenieClass
from genieutils.versions import Version


@dataclass(slots=True)
class Task(GenieClass):
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

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Task':
        return cls(
            task_type=content.read_int_16(),
            id=content.read_int_16(),
            is_default=content.read_int_8(),
            action_type=content.read_int_16(),
            class_id=content.read_int_16(),
            unit_id=content.read_int_16(),
            terrain_id=content.read_int_16(),
            resource_in=content.read_int_16(),
            resource_multiplier=content.read_int_16(),
            resource_out=content.read_int_16(),
            unused_resource=content.read_int_16(),
            work_value_1=content.read_float(),
            work_value_2=content.read_float(),
            work_range=content.read_float(),
            auto_search_targets=content.read_int_8(),
            search_wait_time=content.read_float(),
            enable_targeting=content.read_int_8(),
            combat_level_flag=content.read_int_8(),
            gather_type=content.read_int_16(),
            work_flag_2=content.read_int_16(),
            target_diplomacy=content.read_int_8(),
            carry_check=content.read_int_8(),
            pick_for_construction=content.read_int_8(),
            moving_graphic_id=content.read_int_16(),
            proceeding_graphic_id=content.read_int_16(),
            working_graphic_id=content.read_int_16(),
            carrying_graphic_id=content.read_int_16(),
            resource_gathering_sound_id=content.read_int_16(),
            resource_deposit_sound_id=content.read_int_16(),
            wwise_resource_gathering_sound_id=content.read_int_32(),
            wwise_resource_deposit_sound_id=content.read_int_32(),
        )

    def to_bytes(self, version: Version) -> bytes:
        return b''.join([
            self.write_int_16(self.task_type),
            self.write_int_16(self.id),
            self.write_int_8(self.is_default),
            self.write_int_16(self.action_type),
            self.write_int_16(self.class_id),
            self.write_int_16(self.unit_id),
            self.write_int_16(self.terrain_id),
            self.write_int_16(self.resource_in),
            self.write_int_16(self.resource_multiplier),
            self.write_int_16(self.resource_out),
            self.write_int_16(self.unused_resource),
            self.write_float(self.work_value_1),
            self.write_float(self.work_value_2),
            self.write_float(self.work_range),
            self.write_int_8(self.auto_search_targets),
            self.write_float(self.search_wait_time),
            self.write_int_8(self.enable_targeting),
            self.write_int_8(self.combat_level_flag),
            self.write_int_16(self.gather_type),
            self.write_int_16(self.work_flag_2),
            self.write_int_8(self.target_diplomacy),
            self.write_int_8(self.carry_check),
            self.write_int_8(self.pick_for_construction),
            self.write_int_16(self.moving_graphic_id),
            self.write_int_16(self.proceeding_graphic_id),
            self.write_int_16(self.working_graphic_id),
            self.write_int_16(self.carrying_graphic_id),
            self.write_int_16(self.resource_gathering_sound_id),
            self.write_int_16(self.resource_deposit_sound_id),
            self.write_int_32(self.wwise_resource_gathering_sound_id),
            self.write_int_32(self.wwise_resource_deposit_sound_id),
        ])
