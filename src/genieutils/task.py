import struct
from dataclasses import dataclass

from genieutils.common import ByteHandler, GenieClass
from genieutils.versions import Version

FORMAT = '<hhbhhhhhhhhfffbfbbhhbbbhhhhhhll'
FORMAT_LENGTH = 67

FORMAT_88 = '<hhbhhhhhhhhfffbfbbhhbbbhhhhhhllh'
FORMAT_LENGTH_88 = struct.calcsize(FORMAT_88)


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
    enabled: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Task':
        if content.version >= Version.VER_88:
            return cls.from_bytes_88(content)
        return cls.from_bytes_84(content)

    @classmethod
    def from_bytes_84(cls, content: ByteHandler) -> 'Task':
        task_type, \
            id_, \
            is_default, \
            action_type, \
            class_id, \
            unit_id, \
            terrain_id, \
            resource_in, \
            resource_multiplier, \
            resource_out, \
            unused_resource, \
            work_value_1, \
            work_value_2, \
            work_range, \
            auto_search_targets, \
            search_wait_time, \
            enable_targeting, \
            combat_level_flag, \
            gather_type, \
            work_flag_2, \
            target_diplomacy, \
            carry_check, \
            pick_for_construction, \
            moving_graphic_id, \
            proceeding_graphic_id, \
            working_graphic_id, \
            carrying_graphic_id, \
            resource_gathering_sound_id, \
            resource_deposit_sound_id, \
            wwise_resource_gathering_sound_id, \
            wwise_resource_deposit_sound_id = struct.unpack(
            FORMAT,
            content.consume_range(FORMAT_LENGTH)
        )

        return cls(
            task_type=task_type,
            id=id_,
            is_default=is_default,
            action_type=action_type,
            class_id=class_id,
            unit_id=unit_id,
            terrain_id=terrain_id,
            resource_in=resource_in,
            resource_multiplier=resource_multiplier,
            resource_out=resource_out,
            unused_resource=unused_resource,
            work_value_1=work_value_1,
            work_value_2=work_value_2,
            work_range=work_range,
            auto_search_targets=auto_search_targets,
            search_wait_time=search_wait_time,
            enable_targeting=enable_targeting,
            combat_level_flag=combat_level_flag,
            gather_type=gather_type,
            work_flag_2=work_flag_2,
            target_diplomacy=target_diplomacy,
            carry_check=carry_check,
            pick_for_construction=pick_for_construction,
            moving_graphic_id=moving_graphic_id,
            proceeding_graphic_id=proceeding_graphic_id,
            working_graphic_id=working_graphic_id,
            carrying_graphic_id=carrying_graphic_id,
            resource_gathering_sound_id=resource_gathering_sound_id,
            resource_deposit_sound_id=resource_deposit_sound_id,
            wwise_resource_gathering_sound_id=wwise_resource_gathering_sound_id,
            wwise_resource_deposit_sound_id=wwise_resource_deposit_sound_id,
            enabled=-1,
        )

    @classmethod
    def from_bytes_88(cls, content: ByteHandler) -> 'Task':
        task_type, \
            id_, \
            is_default, \
            action_type, \
            class_id, \
            unit_id, \
            terrain_id, \
            resource_in, \
            resource_multiplier, \
            resource_out, \
            unused_resource, \
            work_value_1, \
            work_value_2, \
            work_range, \
            auto_search_targets, \
            search_wait_time, \
            enable_targeting, \
            combat_level_flag, \
            gather_type, \
            work_flag_2, \
            target_diplomacy, \
            carry_check, \
            pick_for_construction, \
            moving_graphic_id, \
            proceeding_graphic_id, \
            working_graphic_id, \
            carrying_graphic_id, \
            resource_gathering_sound_id, \
            resource_deposit_sound_id, \
            wwise_resource_gathering_sound_id, \
            wwise_resource_deposit_sound_id, \
            enabled = struct.unpack(
            FORMAT_88,
            content.consume_range(FORMAT_LENGTH_88)
        )

        return cls(
            task_type=task_type,
            id=id_,
            is_default=is_default,
            action_type=action_type,
            class_id=class_id,
            unit_id=unit_id,
            terrain_id=terrain_id,
            resource_in=resource_in,
            resource_multiplier=resource_multiplier,
            resource_out=resource_out,
            unused_resource=unused_resource,
            work_value_1=work_value_1,
            work_value_2=work_value_2,
            work_range=work_range,
            auto_search_targets=auto_search_targets,
            search_wait_time=search_wait_time,
            enable_targeting=enable_targeting,
            combat_level_flag=combat_level_flag,
            gather_type=gather_type,
            work_flag_2=work_flag_2,
            target_diplomacy=target_diplomacy,
            carry_check=carry_check,
            pick_for_construction=pick_for_construction,
            moving_graphic_id=moving_graphic_id,
            proceeding_graphic_id=proceeding_graphic_id,
            working_graphic_id=working_graphic_id,
            carrying_graphic_id=carrying_graphic_id,
            resource_gathering_sound_id=resource_gathering_sound_id,
            resource_deposit_sound_id=resource_deposit_sound_id,
            wwise_resource_gathering_sound_id=wwise_resource_gathering_sound_id,
            wwise_resource_deposit_sound_id=wwise_resource_deposit_sound_id,
            enabled=enabled,
        )

    def to_bytes(self, version: Version) -> bytes:
        if version >= Version.VER_88:
            return self.to_bytes_88(version)
        return self.to_bytes_84(version)


    def to_bytes_84(self, version: Version) -> bytes:
        return struct.pack(FORMAT,
                           self.task_type,
                           self.id,
                           self.is_default,
                           self.action_type,
                           self.class_id,
                           self.unit_id,
                           self.terrain_id,
                           self.resource_in,
                           self.resource_multiplier,
                           self.resource_out,
                           self.unused_resource,
                           self.work_value_1,
                           self.work_value_2,
                           self.work_range,
                           self.auto_search_targets,
                           self.search_wait_time,
                           self.enable_targeting,
                           self.combat_level_flag,
                           self.gather_type,
                           self.work_flag_2,
                           self.target_diplomacy,
                           self.carry_check,
                           self.pick_for_construction,
                           self.moving_graphic_id,
                           self.proceeding_graphic_id,
                           self.working_graphic_id,
                           self.carrying_graphic_id,
                           self.resource_gathering_sound_id,
                           self.resource_deposit_sound_id,
                           self.wwise_resource_gathering_sound_id,
                           self.wwise_resource_deposit_sound_id,
                           )


    def to_bytes_88(self, version: Version) -> bytes:
        return struct.pack(FORMAT_88,
                           self.task_type,
                           self.id,
                           self.is_default,
                           self.action_type,
                           self.class_id,
                           self.unit_id,
                           self.terrain_id,
                           self.resource_in,
                           self.resource_multiplier,
                           self.resource_out,
                           self.unused_resource,
                           self.work_value_1,
                           self.work_value_2,
                           self.work_range,
                           self.auto_search_targets,
                           self.search_wait_time,
                           self.enable_targeting,
                           self.combat_level_flag,
                           self.gather_type,
                           self.work_flag_2,
                           self.target_diplomacy,
                           self.carry_check,
                           self.pick_for_construction,
                           self.moving_graphic_id,
                           self.proceeding_graphic_id,
                           self.working_graphic_id,
                           self.carrying_graphic_id,
                           self.resource_gathering_sound_id,
                           self.resource_deposit_sound_id,
                           self.wwise_resource_gathering_sound_id,
                           self.wwise_resource_deposit_sound_id,
                           self.enabled,
                           )
