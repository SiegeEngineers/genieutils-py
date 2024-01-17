from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.task import Task


@dataclass
class UnitHeaders(GenieClass):
    exists: int
    task_count: int | None = None
    task_list: list[Task] | None = None

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'UnitHeaders':
        super().__init__(content)
        exists = content.read_int_8()
        task_count = None
        task_list = None
        if exists:
            task_count = content.read_int_16()
            task_list = content.read_class_array(Task, task_count)
        return cls(
            exists=exists,
            task_count=task_count,
            task_list=task_list,
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_8(self.exists),
            self.write_int_16(self.task_count) if self.exists else b'',
            self.write_class_array(self.task_list) if self.exists else b'',
        ])
