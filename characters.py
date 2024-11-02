#
#  letter_bytes = {
#     'A': b'\x01\x01\x03\x01\x07\x21\x02\x07\x00',
#     'B': b'\x0F\x03\x04\x0C\x0F\x02\x06\x0C\x01',
#     'C': b'\x06\x02\x06\x0C\x1C\x00\x04\x0E\x00',
#     'D': b'\x0F\x03\x04\x0C\x0E\x06\x06\x0C\x00',
#     'E': b'\x0F\x01\x02\x0C\x09\x20\x00\x1D\x01',
#     'F': b'\x0F\x01\x03\x09\x03\x00\x00\x1D\x00',
#     'G': b'\x06\x06\x04\x0D\x1B\x1C\x06\x0E\x00',
#     'H': b'\x0F\x03\x04\x08\x07\x26\x04\x10\x01',
#     'I': b'\x00\x00\x01\x07\x00\x00\x01\x04\x01',
#     'J': b'\x00\x00\x02\x0D\x0F\x01\x02\x0C\x00',
#     'K': b'\x0F\x03\x04\x09\x04\x20\x03\x10\x01',
#     'L': b'\x0F\x01\x02\x0C\x08\x00\x00\x01\x00',
#     'M': b'\x0F\x1E\x05\x07\x01\x3F\x0C\x31\x00',
#     'N': b'\x0F\x02\x04\x0B\x0E\x26\x04\x13\x01',
#     'O': b'\x06\x06\x04\x0C\x1C\x0E\x06\x0C\x00',
#     'P': b'\x0F\x01\x03\x09\x01\x02\x06\x0D\x00',
#     'Q': b'\x06\x06\x04\x0C\x1C\x0E\x06\x0C\x00',
#     'R': b'\x0F\x03\x04\x09\x05\x22\x04\x0C\x00',
#     'S': b'\x07\x00\x00\x0C\x1F\x00\x06\x0D\x01',
#     'T': b'\x0C\x00\x01\x07\x00\x00\x01\x1C\x01',
#     'U': b'\x0F\x02\x04\x0C\x1E\x06\x04\x10\x00',
#     'V': b'\x07\x01\x03\x07\x01\x02\x04\x11\x00',
#     'W': b'\x00\x1F\x06\x09\x07\x3D\x0B\x26\x00',
#     'X': b'\x0C\x00\x03\x09\x04\x21\x02\x11\x01',
#     'Y': b'\x04\x00\x01\x07\x00\x01\x06\x11\x01',
#     'Z': b'\x0C\x00\x03\x0C\x08\x21\x02\x1C\x01',
# }
CHARACTER_BYTES = {
'A': b'\x00\x80\x83\x0D\x02\x3E\x07\x0C',
'B': b'\x09\x81\x82\x8C\x09\x3E\x0C\x1F',
'C': b'\x01\x01\x02\x04\x08\x30\x08\x3F',
'D': b'\x09\x01\x02\x0C\x08\x1C\x1C\x0F',
'E': b'\x09\x81\x83\x8C\x09\x24\x00\x3F',
'F': b'\x00\x80\x83\x85\x03\x04\x01\x3F',
'G': b'\x01\x01\x02\x04\x0B\x3C\x04\x3F',
'H': b'\x09\x81\x82\x8C\x01\x3C\x08\x23',
'I': b'\x00\x00\x00\x03\x09\x01\x02\x08',
'J': b'\x00\x00\x00\x04\x0E\x06\x04\x18',
'K': b'\x09\x81\x82\x8C\x07\x31\x04\x23',
'L': b'\x00\x80\x83\x84\x08\x20\x01\x03',
'M': b'\x0F\x81\x82\x8B\x0E\x1A\x7D\x63',
'N': b'\x09\x01\x02\x08\x07\x3D\x09\x23',
'O': b'\x01\x01\x02\x04\x08\x18\x3C\x1F',
'P': b'\x09\x01\x03\x0D\x03\x04\x0C\x3F',
'Q': b'\x01\x01\x02\x04\x08\x58\x3C\x1F',
'R': b'\x09\x01\x02\x0C\x03\x34\x08\x3F',
'S': b'\x00\x80\x82\x04\x09\x3C\x04\x1F',
'T': b'\x08\x00\x00\x03\x09\x01\x02\x3C',
'U': b'\x09\x01\x02\x04\x08\x1C\x08\x23',
'V': b'\x08\x80\x81\x82\x0E\x06\x0C\x23',
'W': b'\x07\x81\x83\x8C\x02\x32\x73\x4C',
'X': b'\x08\x00\x01\x0D\x07\x33\x05\x22',
'Y': b'\x08\x80\x80\x83\x09\x02\x05\x22',
'Z': b'\x00\x00\x01\x0D\x09\x23\x04\x3C',
'0': b'\x00\x80\x81\x84\x0C\x0E\x05\x1F',
'1': b'\x00\x00\x00\x01\x0F\x21\x02\x0E',
'2': b'\x00\x00\x00\x07\x09\x22\x05\x1E',
'3': b'\x00\x00\x00\x04\x0B\x1A\x04\x1E',
'4': b'\x00\x80\x82\x82\x06\x2A\x06\x18',
'5': b'\x00\x80\x80\x84\x09\x1F\x01\x1E',
'6': b'\x00\x80\x81\x84\x09\x1E\x05\x1F',
'7': b'\x00\x00\x00\x03\x09\x02\x04\x3C',
'8': b'\x00\x80\x83\x84\x09\x1A\x05\x1F',
'9': b'\x00\x80\x80\x85\x0C\x0E\x05\x1F',
}

def set_character(i2c_bus, letter):
    PETAL_ADDRESS = 0x00

    character_byte = CHARACTER_BYTES[letter]
    i2c_bus.writeto_mem(PETAL_ADDRESS, 1, character_byte)