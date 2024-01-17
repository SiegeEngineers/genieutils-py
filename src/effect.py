import typing
from dataclasses import dataclass

from src.common import ByteHandler, GenieClass
from src.effectcommand import EffectCommand


@dataclass
class Effect(GenieClass):
    name: str
    effect_command_count: int
    effect_commands: list[EffectCommand]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Effect':
        name = content.read_debug_string()
        effect_command_count = content.read_int_16()
        effect_commands = content.read_class_array(EffectCommand, effect_command_count)
        return cls(
            name=name,
            effect_command_count=effect_command_count,
            effect_commands=effect_commands,
        )
