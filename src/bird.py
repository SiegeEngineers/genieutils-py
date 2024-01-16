from dataclasses import dataclass

from src.common import ByteHandler
from src.task import Task


@dataclass
class Bird(ByteHandler):
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

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.default_task_id = self.read_int_16()
        self.search_radius = self.read_float()
        self.work_rate = self.read_float()
        self.drop_sites = self.read_int_16_array(3)
        self.task_swap_group = self.read_int_8()
        self.attack_sound = self.read_int_16()
        self.move_sound = self.read_int_16()
        self.wwise_attack_sound_id = self.read_int_32()
        self.wwise_move_sound_id = self.read_int_32()
        self.run_pattern = self.read_int_8()
        self.task_size = self.read_int_16()
        self.tasks = self.read_class_array(Task, self.task_size)
