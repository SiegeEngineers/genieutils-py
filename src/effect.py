from dataclasses import dataclass

from src.common import ByteHandler
from src.effectcommand import EffectCommand
from src.mapinfo import MapInfo


@dataclass
class Effect(ByteHandler):
    name: str
    effect_command_count: int
    effect_commands: list[EffectCommand]

    def __init__(self, content: memoryview):
        super().__init__(content)
        self.name = self.read_debug_string()
        self.effect_command_count = self.read_int_16()
        self.effect_commands = self.read_effect_command_array(self.effect_command_count)

    def read_effect_command_array(self, size: int) -> list[EffectCommand]:
        elements = []
        for i in range(size):
            effect_command = EffectCommand(self.content[self.offset:])
            elements.append(effect_command)
            self.offset += effect_command.offset
        return elements
