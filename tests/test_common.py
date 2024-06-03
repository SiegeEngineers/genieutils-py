import dataclasses

import pytest

from genieutils.common import GenieClass, ByteHandler
from genieutils.versions import Version

class TestGenieClass:
    @pytest.fixture
    def genie_class(self):
        return GenieClass()
    
    def test_from_bytes(self, genie_class: GenieClass):
        with pytest.raises(NotImplementedError):
            genie_class.from_bytes(ByteHandler(b''))

    def test_from_bytes_with_count(self, genie_class: GenieClass):
        with pytest.raises(NotImplementedError):
            genie_class.from_bytes_with_count(ByteHandler(b''), 0)

    def test_to_bytes(self, genie_class: GenieClass):
        with pytest.raises(NotImplementedError):
            genie_class.to_bytes(Version.UNDEFINED)

    def test_write_debug_string(self, genie_class: GenieClass):
        assert genie_class.write_debug_string("foobar") == b'\x60\x0A\x06\x00foobar'

    def test_write_string(self, genie_class: GenieClass):
        assert genie_class.write_string(6, "foobar") == b'foobar'

    def test_write_int_8(self, genie_class: GenieClass):
        assert genie_class.write_int_8(10) == b'\x0A'
        with pytest.raises(OverflowError):
            genie_class.write_int_8(1000)

    def test_write_int_8_array(self, genie_class: GenieClass):
        assert genie_class.write_int_8_array([10, 10, 10]) == b'\x0A\x0A\x0A'
        with pytest.raises(OverflowError):
            genie_class.write_int_8_array([10, 10, 1000])

    def test_write_int_16(self, genie_class: GenieClass):
        assert genie_class.write_int_16(10) == b'\x0A\x00'
        with pytest.raises(OverflowError):
            genie_class.write_int_16(70000)

    def test_write_int_16_array(self, genie_class: GenieClass):
        assert genie_class.write_int_16_array([10, 10, 10]) == b'\x0A\x00\x0A\x00\x0A\x00'
        with pytest.raises(OverflowError):
            genie_class.write_int_16_array([10, 10, 70000])

    def test_write_int_32(self, genie_class: GenieClass):
        assert genie_class.write_int_32(10) == b'\x0A\x00\x00\x00'
        with pytest.raises(OverflowError):
            genie_class.write_int_32(5000000000)

    def test_write_int_32_array(self, genie_class: GenieClass):
        assert genie_class.write_int_32_array([10, 10, 10]) == b'\x0A\x00\x00\x00\x0A\x00\x00\x00\x0A\x00\x00\x00'
        with pytest.raises(OverflowError):
            genie_class.write_int_32_array([10, 10, 5000000000])

    def test_write_float(self, genie_class: GenieClass):
        assert genie_class.write_float(10) == b'\x00\x00\x20\x41'

    def test_write_float_array(self, genie_class: GenieClass):
        assert genie_class.write_float_array([10, 10, 10]) == b'\x00\x00\x20\x41\x00\x00\x20\x41\x00\x00\x20\x41'

    def test_write_class(self, genie_class: GenieClass):
        with pytest.raises(NotImplementedError):
            genie_class.write_class(GenieClass(), Version.UNDEFINED)

    def test_write_class_array(self, genie_class: GenieClass):
        with pytest.raises(NotImplementedError):
            genie_class.write_class(GenieClass(), Version.UNDEFINED)


class TestByteHandler:
    @pytest.fixture
    def byte_handler_8(self):
        data = memoryview(b''.join([int.to_bytes(i) for i in range(32)]))
        return ByteHandler(data)
    
    @pytest.fixture
    def byte_handler_16(self):
        data = memoryview(b''.join([int.to_bytes(i) + b'\x00' for i in range(32)]))
        return ByteHandler(data)
    
    @pytest.fixture
    def byte_handler_32(self):
        data = memoryview(b''.join([int.to_bytes(i) + b'\x00\x00\x00' for i in range(32)]))
        return ByteHandler(data)
    
    @pytest.fixture
    def byte_handler_float(self):
        data = memoryview(b'\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00\x00\x40' * 32)
        return ByteHandler(data)
    
    @pytest.fixture
    def byte_handler_class(self):
        data = memoryview(b'\x80\x01\x00\x00\x08\x00\x00\x46\x4f\x4f\x42\x41\x52\x00\x00\x80\x3f' * 32)
        return ByteHandler(data)
    
    @pytest.fixture
    def child_genie_class(self):
        @dataclasses.dataclass
        class ChildGenieClass(GenieClass):
            int_8_val: int
            int_16_val: int
            int_32_val: int
            str_val: str
            float_val: float
            
            @classmethod
            def from_bytes(cls, data: 'ByteHandler'):
                return cls(
                    int_8_val = data.read_int_8(),
                    int_16_val = data.read_int_16(),
                    int_32_val = data.read_int_32(),
                    str_val = data.read_string(6),
                    float_val = data.read_float(),
                )
                
        return ChildGenieClass
    
    def test_consume_range(self, byte_handler_8: ByteHandler):
        assert bytes(byte_handler_8.consume_range(10)) == b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'

    def test_read_debug_string(self, byte_handler_8: ByteHandler):
        ...

    def test_read_string(self, byte_handler_8: ByteHandler):
        assert byte_handler_8.read_string(10) == '\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'

    def test_read_int_8(self, byte_handler_8: ByteHandler):
        assert byte_handler_8.read_int_8() == 0

    def test_read_int_8_array(self, byte_handler_8: ByteHandler):
        assert byte_handler_8.read_int_8_array(3) == [0, 1, 2]

    def test_read_int_8_array_2(self, byte_handler_8: ByteHandler):
        assert byte_handler_8.read_int_8_array_2() == (0, 1)

    def test_read_int_8_array_3(self, byte_handler_8: ByteHandler):
        assert byte_handler_8.read_int_8_array_3() == (0, 1, 2)

    def test_read_int_8_array_5(self, byte_handler_8: ByteHandler):
        assert byte_handler_8.read_int_8_array_5() == (0, 1, 2, 3, 4)

    def test_read_int_8_array_6(self, byte_handler_8: ByteHandler):
        assert byte_handler_8.read_int_8_array_6() == (0, 1, 2, 3, 4, 5)

    def test_read_int_8_array_10(self, byte_handler_8: ByteHandler):
        assert byte_handler_8.read_int_8_array_10() == (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_read_int_16(self, byte_handler_16: ByteHandler):
        assert byte_handler_16.read_int_16() == 0
        assert byte_handler_16.read_int_16(False) == 1

    def test_read_int_16_array(self, byte_handler_16: ByteHandler):
        assert byte_handler_16.read_int_16_array(3) == [0, 1, 2]

    def test_read_int_16_array_2(self, byte_handler_16: ByteHandler):
        assert byte_handler_16.read_int_16_array_2() == (0, 1)

    def test_read_int_16_array_3(self, byte_handler_16: ByteHandler):
        assert byte_handler_16.read_int_16_array_3() == (0, 1, 2)

    def test_read_int_16_array_4(self, byte_handler_16: ByteHandler):
        assert byte_handler_16.read_int_16_array_4() == (0, 1, 2, 3)
        
    def test_read_int_16_array_6(self, byte_handler_16: ByteHandler):
        assert byte_handler_16.read_int_16_array_6() == (0, 1, 2, 3, 4, 5)

    def test_read_int_32(self, byte_handler_32: ByteHandler):
        assert byte_handler_32.read_int_32() == 0
        assert byte_handler_32.read_int_32(False) == 1

    def test_read_int_32_array(self, byte_handler_32: ByteHandler):
        assert byte_handler_32.read_int_32_array(3) == [0, 1, 2]

    def test_read_int_32_array_10(self, byte_handler_32: ByteHandler):
        assert byte_handler_32.read_int_32_array_10() == (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_read_float(self, byte_handler_float: ByteHandler):
        assert byte_handler_float.read_float() == 0.0

    def test_read_float_array(self, byte_handler_float: ByteHandler):
        assert byte_handler_float.read_float_array(3) == [0.0, 1.0, 2.0]

    def test_read_float_array_2(self, byte_handler_float: ByteHandler):
        assert byte_handler_float.read_float_array_2() == (0.0, 1.0)

    def test_read_float_array_3(self, byte_handler_float: ByteHandler):
        assert byte_handler_float.read_float_array_3() == (0.0, 1.0, 2.0)

    def test_read_class(self, byte_handler_class: ByteHandler, child_genie_class):
        read_class = byte_handler_class.read_class(child_genie_class)
        assert isinstance(read_class, child_genie_class)
        assert read_class.int_8_val == 128
        assert read_class.int_16_val == 1
        assert read_class.int_32_val == 2048
        assert read_class.str_val == 'FOOBAR'
        assert read_class.float_val == 1.0

    def test_read_class_array(self, byte_handler_class: ByteHandler, child_genie_class):
        read_classes = byte_handler_class.read_class_array(child_genie_class, 3)
        assert len(read_classes) == 3
        
        for read_class in read_classes:
            assert isinstance(read_class, child_genie_class)
            assert read_class.int_8_val == 128
            assert read_class.int_16_val == 1
            assert read_class.int_32_val == 2048
            assert read_class.str_val == 'FOOBAR'
            assert read_class.float_val == 1.0
        

    def test_read_class_array_3(self, byte_handler_class: ByteHandler, child_genie_class):
        read_classes = byte_handler_class.read_class_array_3(child_genie_class)
        assert len(read_classes) == 3
        
        for read_class in read_classes:
            assert isinstance(read_class, child_genie_class)
            assert read_class.int_8_val == 128
            assert read_class.int_16_val == 1
            assert read_class.int_32_val == 2048
            assert read_class.str_val == 'FOOBAR'
            assert read_class.float_val == 1.0

    def test_read_class_array_4(self, byte_handler_class: ByteHandler, child_genie_class):
        read_classes = byte_handler_class.read_class_array_4(child_genie_class)
        assert len(read_classes) == 4
        
        for read_class in read_classes:
            assert isinstance(read_class, child_genie_class)
            assert read_class.int_8_val == 128
            assert read_class.int_16_val == 1
            assert read_class.int_32_val == 2048
            assert read_class.str_val == 'FOOBAR'
            assert read_class.float_val == 1.0

    def test_read_class_array_with_pointers(self, byte_handler_8: ByteHandler, child_genie_class):
        ...

    def test_read_class_array_with_param(self, byte_handler_8: ByteHandler, child_genie_class):
        ...
