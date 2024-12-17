from dataclasses import dataclass

from genieutils.common import ByteHandler, GenieClass
from genieutils.task import Task
from genieutils.versions import Version


@dataclass(slots=True)
class UnitHeaders(GenieClass):
    exists: int
    task_list: list[Task] | None = None

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'UnitHeaders':
        exists = content.read_int_8()
        task_list = None
        if exists:
            task_count = content.read_int_16()
            task_list = content.read_class_array(Task, task_count)
        return cls(
            exists=exists,
            task_list=task_list,
        )

    def to_bytes(self, version: Version) -> bytes:
        return b''.join([
            self.write_int_8(self.exists),
            self.write_int_16(len(self.task_list)) if self.exists and self.task_list is not None else b'',
            self.write_class_array(self.task_list, version) if self.exists and self.task_list is not None else b'',
        ])
