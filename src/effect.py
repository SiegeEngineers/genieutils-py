from dataclasses import dataclass

from src.common import ByteHandler
from src.effectcommand import EffectCommand


@dataclass
class Effect(ByteHandler):
    name: str
    effect_command_count: int
    effect_commands: list[EffectCommand]

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.name = self.read_debug_string()
        self.effect_command_count = self.read_int_16()
        self.effect_commands = self.read_class_array(EffectCommand, self.effect_command_count)
