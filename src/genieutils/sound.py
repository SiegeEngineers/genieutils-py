from dataclasses import dataclass

from genieutils.common import ByteHandler, GenieClass


@dataclass
class SoundItem(GenieClass):
    filename: str
    resource_id: int
    probability: int
    civilization: int
    icon_set: int

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'SoundItem':
        return cls(
            filename=content.read_debug_string(),
            resource_id=content.read_int_32(),
            probability=content.read_int_16(),
            civilization=content.read_int_16(),
            icon_set=content.read_int_16(),
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_debug_string(self.filename),
            self.write_int_32(self.resource_id),
            self.write_int_16(self.probability),
            self.write_int_16(self.civilization),
            self.write_int_16(self.icon_set),
        ])


@dataclass
class Sound(GenieClass):
    id: int
    play_delay: int
    cache_time: int
    total_probability: int
    items: list[SoundItem]

    @classmethod
    def from_bytes(cls, content: ByteHandler) -> 'Sound':
        id_ = content.read_int_16()
        play_delay = content.read_int_16()
        items_size = content.read_int_16()
        cache_time = content.read_int_32()
        total_probability = content.read_int_16()
        items = content.read_class_array(SoundItem, items_size)
        return cls(
            id=id_,
            play_delay=play_delay,
            cache_time=cache_time,
            total_probability=total_probability,
            items=items,
        )

    def to_bytes(self) -> bytes:
        return b''.join([
            self.write_int_16(self.id),
            self.write_int_16(self.play_delay),
            self.write_int_16(len(self.items)),
            self.write_int_32(self.cache_time),
            self.write_int_16(self.total_probability),
            self.write_class_array(self.items),
        ])
