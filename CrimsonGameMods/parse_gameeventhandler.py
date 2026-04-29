import struct

def parse_gameeventhandler_entry(data, pos):
    """Auto-generated parser for gameeventhandler entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_4'] = data[pos]; pos += 1
    entry['field_5'] = data[pos]; pos += 1
    entry['field_6'] = data[pos]; pos += 1
    entry['field_7'] = data[pos]; pos += 1
    entry['field_8'] = data[pos]; pos += 1
    entry['field_9'] = data[pos]; pos += 1
    entry['field_10'] = data[pos]; pos += 1
    entry['field_11'] = data[pos]; pos += 1
    entry['field_12'] = data[pos]; pos += 1

    return entry, pos
