from enum import Enum


class Version(Enum):
    UNDEFINED = 'UNDEFINED'
    VER_71 = 'VER 7.1'
    VER_72 = 'VER 7.2'
    VER_73 = 'VER 7.3'
    VER_74 = 'VER 7.4'
    VER_75 = 'VER 7.5'
    VER_76 = 'VER 7.6'
    VER_77 = 'VER 7.7'
    VER_78 = 'VER 7.8'
    VER_84 = 'VER 8.4'
    VER_88 = 'VER 8.8'

    def __lt__(self, other: 'Version'):
        return self.value < other.value

    def __le__(self, other: 'Version'):
        return self.value <= other.value

    def __gt__(self, other: 'Version'):
        return self.value > other.value

    def __ge__(self, other: 'Version'):
        return self.value >= other.value
