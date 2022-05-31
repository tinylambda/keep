import struct
import ctypes
import binascii


class BitUtil:
    """
    Process bits in a bytes buffer
    """

    ONE_BYTE_STRUCT = struct.Struct("1b")

    @classmethod
    def get_location_info(cls, bytes_buffer, nth):
        buffer_length_in_bytes = len(bytes_buffer)
        buffer_length_in_bit = buffer_length_in_bytes * 8
        assert buffer_length_in_bit >= nth
        nth_0_based = nth - 1
        assert nth_0_based >= 0

        byte_location, bit_location = divmod(nth_0_based, 8)
        return byte_location, bit_location

    @classmethod
    def set_bit(cls, bytes_buffer, nth):
        """
        :param bytes_buffer: bytes buffer to be modified
        :param nth: 1-based index, should be smaller than the length of bytes_buffer in bit
        :return: None
        """
        byte_location, bit_location = cls.get_location_info(bytes_buffer, nth)
        byte_selected = bytes_buffer[byte_location]
        byte_selected_value = cls.ONE_BYTE_STRUCT.unpack(byte_selected)[0]

        mask_bits = ["0" for _ in range(8)]
        mask_bits[bit_location] = "1"
        mask_byte_string = "".join(mask_bits)
        mask_byte_value = int(mask_byte_string, 2)

        byte_selected_masked = byte_selected_value | mask_byte_value
        bytes_buffer[byte_location] = byte_selected_masked

    @classmethod
    def reset_bit(cls, bytes_buffer, nth):
        byte_location, bit_location = cls.get_location_info(bytes_buffer, nth)
        byte_selected = bytes_buffer[byte_location]
        byte_selected_value = cls.ONE_BYTE_STRUCT.unpack(byte_selected)[0]

        mask_bits = ["1" for _ in range(8)]
        mask_bits[bit_location] = "0"
        mask_byte_string = "".join(mask_bits)
        mask_byte_value = int(mask_byte_string, 2)

        byte_selected_masked = byte_selected_value & mask_byte_value
        bytes_buffer[byte_location] = byte_selected_masked

    @classmethod
    def get_bit(cls, bytes_buffer, nth):
        byte_location, bit_location = cls.get_location_info(bytes_buffer, nth)
        byte_selected = bytes_buffer[byte_location]
        byte_selected_value = cls.ONE_BYTE_STRUCT.unpack(byte_selected)[0]

        mask_bits = ["0" for _ in range(8)]
        mask_bits[bit_location] = "1"
        mask_byte_string = "".join(mask_bits)
        mask_byte_value = int(mask_byte_string, 2)

        byte_selected_masked = byte_selected_value & mask_byte_value
        if byte_selected_masked > 0:
            return "1"
        else:
            return "0"

    @classmethod
    def set_bit_batch(cls, bytes_buffer, nth_list=[]):
        for nth in nth_list:
            cls.set_bit(bytes_buffer, nth)

    @classmethod
    def reset_bit_batch(cls, bytes_buffer, nth_list):
        for nth in nth_list:
            cls.reset_bit(bytes_buffer, nth)

    @classmethod
    def get_bit_batch(cls, bytes_buffer, nth_list):
        bit_value_list = [cls.get_bit(bytes_buffer, nth) for nth in nth_list]
        return "".join(bit_value_list)

    @classmethod
    def set_byte(cls, bytes_buffer, nth, value):
        bytes_buffer[nth - 1] = value

    @classmethod
    def get_byte(cls, bytes_buffer, nth):
        return bytes_buffer[nth - 1]


class MessageLayout:
    def __init__(self):
        self.blocks = {}

    def add_block(self, name, bit_index_list):
        self.blocks.update({name: {"bit_index_list": bit_index_list}})

    def extract_block(self, name, message):
        block = self.blocks.get(name, {})
        bit_index_list = block.get("bit_index_list", [])
        return BitUtil.get_bit_batch(message, bit_index_list)

    def extract_blocks(
        self,
    ):
        raise NotImplementedError


class StunMessage:
    MAGIC_COOKIE_VALUE = 0x2112A442
    MAGIC_COOKIE_VALUE_HEX = [0x21, 0x12, 0xA4, 0x42]
    MESSAGE_LAYOUT = MessageLayout()
    MESSAGE_LAYOUT.add_block("first_2_bits", [1, 2])
    MESSAGE_LAYOUT.add_block("method_bits", [3, 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16])
    MESSAGE_LAYOUT.add_block("class_bits", [8, 12])
    MESSAGE_LAYOUT.add_block("message_length_bits", [i for i in range(17, 33)])
    MESSAGE_LAYOUT.add_block("magic_cookie_bits", [i for i in range(33, 65)])

    def __init__(self, message):
        self.message = message

    def set_magic_cookie(self):
        # The magic cookie field MUST contain the fixed value 0x2112A442 in network byte order.
        BitUtil.set_byte(self.message, 5, 0x21)
        BitUtil.set_byte(self.message, 6, 0x12)
        BitUtil.set_byte(self.message, 7, 0xA4)
        BitUtil.set_byte(self.message, 8, 0x42)


if __name__ == "__main__":
    s = struct.Struct("20b")
    buffer = ctypes.create_string_buffer(s.size)
    # s.pack_into(buffer, 0, *[i for i in range(20)])
    # print(buffer.raw)
    # BitUtil.set(buffer, 4)
    # print(BitUtil.get(buffer, 4))
    # print(buffer.raw)
    # BitUtil.reset(buffer, 4)
    # print(buffer.raw)
    # print(BitUtil.get(buffer, 4))
    #
    # BitUtil.set(buffer, 160)
    # print(buffer.raw)
    # BitUtil.reset(buffer, 160)
    # print(buffer.raw)
    # BitUtil.set(buffer, 152)
    # print(buffer.raw)
    #
    # print(BitUtil.get_batch(buffer))
    sm = StunMessage(buffer)
    print(binascii.hexlify(sm.message.raw))
