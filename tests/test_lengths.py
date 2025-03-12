import struct

from genieutils import task, unit


class TestLenghts:

    def test_task_length(self):
        assert struct.calcsize(task.FORMAT) == task.FORMAT_LENGTH

    def test_unit_lengths(self):
        assert struct.calcsize(unit.FORMAT) == unit.FORMAT_LENGTH
        assert struct.calcsize(unit.RESOURCE_STORAGE_FORMAT) == unit.RESOURCE_STORAGE_FORMAT_LENGTH
        assert struct.calcsize(unit.DAMAGE_GRAPHIC_FORMAT) == unit.DAMAGE_GRAPHIC_FORMAT_LENGTH
        assert struct.calcsize(unit.DEAD_FISH_FORMAT) == unit.DEAD_FISH_FORMAT_LENGTH
        assert struct.calcsize(unit.RESOURCE_COST_FORMAT) == unit.RESOURCE_COST_FORMAT_LENGTH
        assert struct.calcsize(unit.CREATABLE_FORMAT) == unit.CREATABLE_FORMAT_LENGTH
        assert struct.calcsize(unit.BUILDING_ANNEX_FORMAT) == unit.BUILDING_ANNEX_FORMAT_LENGTH
        assert struct.calcsize(unit.ATTACK_OR_ARMOR_FORMAT) == unit.ATTACK_OR_ARMOR_FORMAT_LENGTH
        assert struct.calcsize(unit.BUILDING_ANNEX_FORMAT_1) == unit.BUILDING_ANNEX_FORMAT_1_LENGTH
        assert struct.calcsize(unit.BUILDING_ANNEX_FORMAT_2) == unit.BUILDING_ANNEX_FORMAT_2_LENGTH
