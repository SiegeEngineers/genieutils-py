from dataclasses import dataclass

from genieutils.common import ByteHandler, GenieClass


@dataclass
class EffectCommand(GenieClass):
    type: int
    a: int
    b: int
    c: int
    d: float

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'EffectCommand':
        return cls(
            type=content.read_int_8(),
            a=content.read_int_16(),
            b=content.read_int_16(),
            c=content.read_int_16(),
            d=content.read_float(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_8(self.type),
            self.write_int_16(self.a),
            self.write_int_16(self.b),
            self.write_int_16(self.c),
            self.write_float(self.d),
        ])


@dataclass
class Effect(GenieClass):
    name: str
    effect_commands: list[EffectCommand]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Effect':
        name = content.read_debug_string()
        effect_command_count = content.read_int_16()
        effect_commands = content.read_class_array(EffectCommand, effect_command_count)
        return cls(
            name=name,
            effect_commands=effect_commands,
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_debug_string(self.name),
            self.write_int_16(len(self.effect_commands)),
            self.write_class_array(self.effect_commands),
        ])
