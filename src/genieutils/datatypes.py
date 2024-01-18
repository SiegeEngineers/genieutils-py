import struct


class String:
    @staticmethod
    def from_bytes(content: memoryview) -> str:
        return bytes(content).rstrip(b'\0').decode()

    @staticmethod
    def to_bytes(content: str, length=None) -> bytes:
        encoded = content.encode()
        if not length:
            length = len(encoded) + 1
        zfill = length - len(encoded)
        return encoded + (b'\0' * zfill)


class Int:
    @staticmethod
    def from_bytes(content: memoryview, signed=True) -> int:
        return int.from_bytes(content, byteorder='little', signed=signed)

    @staticmethod
    def to_bytes(content: int, length=2, signed=True) -> bytes:
        return content.to_bytes(length, 'little', signed=signed)


class Float:
    @staticmethod
    def from_bytes(content: memoryview) -> float:
        return struct.unpack('f', content)[0]

    @staticmethod
    def to_bytes(content: float) -> bytes:
        return struct.pack('f', content)
