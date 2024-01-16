from dataclasses import dataclass

from src.common import ByteHandler
from src.task import Task


@dataclass
class UnitHeaders(ByteHandler):
    exists: int
    task_count: int | None = None
    task_list: list[Task] | None = None

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.exists = self.read_int_8()
        if self.exists:
            self.task_count = self.read_int_16()
            self.task_list = self.read_task_array(self.task_count)

    def read_task_array(self, size: int) -> list[Task]:
        elements = []
        for i in range(size):
            task = Task(self.content[self.offset:])
            elements.append(task)
            self.offset += task.offset
        return elements
