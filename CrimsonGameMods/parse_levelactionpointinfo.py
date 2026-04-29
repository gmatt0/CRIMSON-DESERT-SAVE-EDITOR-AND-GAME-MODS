import struct

def parse_levelactionpointinfo_entry(data, pos):
    """Auto-generated parser for levelactionpointinfo entries."""
    entry = {}

    entry['field_0'] = data[pos]; pos += 1
    entry['field_1'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_3'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_4'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_5'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_6'] = struct.unpack_from('<I', data, pos)[0]; pos += 4

    return entry, pos
