import struct

def parse_failmessageinfo_entry(data, pos):
    """Auto-generated parser for failmessageinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = data[pos]; pos += 1
    entry['field_4'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_5'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_6'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_7'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_8'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_9'] = struct.unpack_from('<f', data, pos)[0]; pos += 4

    return entry, pos
