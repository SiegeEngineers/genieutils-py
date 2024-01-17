import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.task import Task


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
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
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
