import dataclasses

import pytest

from genieutils.common import GenieClass, ByteHandler
from genieutils.versions import Version

class TestGenieClass:
    @pytest.fixture
    def genie_class(self):
        return GenieClass()
        
    def test_write_debug_string(self, genie_class: GenieClass):
        assert genie_class.write_debug_string("foobar") == b'`\n\x06\x00foobar'

    def test_write_string(self, genie_class: GenieClass):
        assert genie_class.write_string(6, "foobar") == b'foobar'

    def test_write_int_8(self, genie_class: GenieClass):
        assert genie_class.write_int_8(10) == b'\n'
        with pytest.raises(OverflowError):
            genie_class.write_int_8(1000)

    def test_write_int_8_array(self, genie_class: GenieClass):
        assert genie_class.write_int_8_array([10, 10, 10]) == b'\n\n\n'
        with pytest.raises(OverflowError):
            genie_class.write_int_8_array([10, 10, 1000])

    def test_write_int_16(self, genie_class: GenieClass):
        assert genie_class.write_int_16(10) == b'\n\x00'
        with pytest.raises(OverflowError):
            genie_class.write_int_16(70000)

    def test_write_int_16_array(self, genie_class: GenieClass):
        assert genie_class.write_int_16_array([10, 10, 10]) == b'\n\x00\n\x00\n\x00'
        with pytest.raises(OverflowError):
            genie_class.write_int_16_array([10, 10, 70000])

    def test_write_int_32(self, genie_class: GenieClass):
        assert genie_class.write_int_32(10) == b'\n\x00\x00\x00'
        with pytest.raises(OverflowError):
            genie_class.write_int_32(5000000000)

    def test_write_int_32_array(self, genie_class: GenieClass):
        assert genie_class.write_int_32_array([10, 10, 10]) == b'\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00'
        with pytest.raises(OverflowError):
            genie_class.write_int_32_array([10, 10, 5000000000])

    def test_write_float(self, genie_class: GenieClass):
        assert genie_class.write_float(10) == b'\x00\x00 A'

    def test_write_float_array(self, genie_class: GenieClass):
        assert genie_class.write_float_array([10, 10, 10]) == b'\x00\x00 A\x00\x00 A\x00\x00 A'

    def test_write_class(self, genie_class: GenieClass):
        with pytest.raises(NotImplementedError):
            genie_class.write_class(GenieClass(), Version.UNDEFINED)

    def test_write_class_array(self, genie_class: GenieClass):
        with pytest.raises(NotImplementedError):
            genie_class.write_class(GenieClass(), Version.UNDEFINED)


class TestByteHandler:
    @pytest.fixture
    def byte_handler(self):
        data = memoryview(b''.join([int.to_bytes(i) for i in range(256)]))
        return ByteHandler(data)
    
    @pytest.fixture
    def child_genie_class(self):
        @dataclasses.dataclass
        class ChildGenieClass(GenieClass):
            int_val: int
            str_val: str
            float_val: float
            
            @classmethod
            def from_bytes(cls, data: 'ByteHandler'):
                return cls(
                    int_val = data.read_int_16(),
                    str_val = data.read_string(5),
                    float_val = data.read_float(),
                )
                
        return ChildGenieClass
    
    def test_consume_range(self, byte_handler: ByteHandler):
        assert bytes(byte_handler.consume_range(10)) == b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t'

    def test_read_debug_string(self, byte_handler: ByteHandler):
        ...

    def test_read_string(self, byte_handler: ByteHandler):
        assert byte_handler.read_string(10) == '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t'

    def test_read_int_8(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_8() == 0

    def test_read_int_8_array(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_8_array(3) == [0, 1, 2]

    def test_read_int_8_array_2(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_8_array_2() == (0, 1)

    def test_read_int_8_array_3(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_8_array_3() == (0, 1, 2)

    def test_read_int_8_array_5(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_8_array_5() == (0, 1, 2, 3, 4)

    def test_read_int_8_array_6(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_8_array_6() == (0, 1, 2, 3, 4, 5)

    def test_read_int_8_array_10(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_8_array_10() == (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_read_int_16(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_16() == 256
        assert byte_handler.read_int_16(False) == 770

    def test_read_int_16_array(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_16_array(3) == [256, 770, 1284]

    def test_read_int_16_array_2(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_16_array_2() == (256, 770)

    def test_read_int_16_array_3(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_16_array_3() == (256, 770, 1284)

    def test_read_int_16_array_4(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_16_array_4() == (256, 770, 1284, 1798)
        
    def test_read_int_16_array_6(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_16_array_6() == (256, 770, 1284, 1798, 2312, 2826)

    def test_read_int_32(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_32() == 50462976
        assert byte_handler.read_int_32(False) == 117835012

    def test_read_int_32_array(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_32_array(3) == [50462976, 117835012, 185207048]

    def test_read_int_32_array_10(self, byte_handler: ByteHandler):
        assert byte_handler.read_int_32_array_10() == (50462976, 117835012, 185207048, 252579084, 319951120, 
                                                       387323156, 454695192, 522067228, 589439264, 656811300)

    def test_read_float(self, byte_handler: ByteHandler):
        assert byte_handler.read_float() == 3.820471434542632e-37

    def test_read_float_array(self, byte_handler: ByteHandler):
        assert byte_handler.read_float_array(3) == [3.820471434542632e-37, 
                                                    1.0082513512365273e-34, 
                                                    2.658462758989161e-32]

    def test_read_float_array_2(self, byte_handler: ByteHandler):
        assert byte_handler.read_float_array_2() == (3.820471434542632e-37, 
                                                    1.0082513512365273e-34)

    def test_read_float_array_3(self, byte_handler: ByteHandler):
        assert byte_handler.read_float_array_3() == (3.820471434542632e-37, 
                                                    1.0082513512365273e-34, 
                                                    2.658462758989161e-32)

    def test_read_class(self, byte_handler: ByteHandler, child_genie_class):
        read_class = byte_handler.read_class(child_genie_class)
        assert isinstance(read_class, child_genie_class)
        assert read_class.int_val == 256
        assert read_class.str_val == '\x02\x03\x04\x05\x06'
        assert read_class.float_val == 6.59781983508312e-33

    def test_read_class_array(self, byte_handler: ByteHandler, child_genie_class):
        read_classes = byte_handler.read_class_array(child_genie_class, 3)
        assert len(read_classes) == 3
        
        assert isinstance(read_classes[0], child_genie_class)
        assert read_classes[0].int_val == 256
        assert read_classes[0].str_val == '\x02\x03\x04\x05\x06'
        assert read_classes[0].float_val == 6.59781983508312e-33
        
        assert isinstance(read_classes[1], child_genie_class)
        assert read_classes[1].int_val == 3083
        assert read_classes[1].str_val == '\r\x0e\x0f\x10\x11'
        assert read_classes[1].float_val == 2.990340580099529e-26
        
        assert isinstance(read_classes[2], child_genie_class)
        assert read_classes[2].int_val == 5910
        assert read_classes[2].str_val == '\x18\x19\x1a\x1b\x1c'
        assert read_classes[2].float_val == 1.3477787510315518e-19
        

    def test_read_class_array_3(self, byte_handler: ByteHandler, child_genie_class):
        read_classes = byte_handler.read_class_array_3(child_genie_class)
        assert len(read_classes) == 3
        
        assert isinstance(read_classes[0], child_genie_class)
        assert read_classes[0].int_val == 256
        assert read_classes[0].str_val == '\x02\x03\x04\x05\x06'
        assert read_classes[0].float_val == 6.59781983508312e-33
        
        assert isinstance(read_classes[1], child_genie_class)
        assert read_classes[1].int_val == 3083
        assert read_classes[1].str_val == '\r\x0e\x0f\x10\x11'
        assert read_classes[1].float_val == 2.990340580099529e-26
        
        assert isinstance(read_classes[2], child_genie_class)
        assert read_classes[2].int_val == 5910
        assert read_classes[2].str_val == '\x18\x19\x1a\x1b\x1c'
        assert read_classes[2].float_val == 1.3477787510315518e-19

    def test_read_class_array_4(self, byte_handler: ByteHandler, child_genie_class):
        read_classes = byte_handler.read_class_array_4(child_genie_class)
        assert len(read_classes) == 4
        
        assert isinstance(read_classes[0], child_genie_class)
        assert read_classes[0].int_val == 256
        assert read_classes[0].str_val == '\x02\x03\x04\x05\x06'
        assert read_classes[0].float_val == 6.59781983508312e-33
        
        assert isinstance(read_classes[1], child_genie_class)
        assert read_classes[1].int_val == 3083
        assert read_classes[1].str_val == '\r\x0e\x0f\x10\x11'
        assert read_classes[1].float_val == 2.990340580099529e-26
        
        assert isinstance(read_classes[2], child_genie_class)
        assert read_classes[2].int_val == 5910
        assert read_classes[2].str_val == '\x18\x19\x1a\x1b\x1c'
        assert read_classes[2].float_val == 1.3477787510315518e-19
        
        assert isinstance(read_classes[3], child_genie_class)
        assert read_classes[3].int_val == 8737
        assert read_classes[3].str_val == "#$%&'"
        assert read_classes[3].float_val == 6.045324831005505e-13

    def test_read_class_array_with_pointers(self, byte_handler: ByteHandler, child_genie_class):
        ...

    def test_read_class_array_with_param(self, byte_handler: ByteHandler, child_genie_class):
        ...
