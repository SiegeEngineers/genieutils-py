import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.task import Task


@dataclass
class UnitHeaders(GenieClass):
    exists: int
    task_count: int | None = None
    task_list: list[Task] | None = None

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> typing.Self:
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
