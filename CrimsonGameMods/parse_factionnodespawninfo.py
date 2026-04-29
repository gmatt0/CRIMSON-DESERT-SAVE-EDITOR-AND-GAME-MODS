import struct

def parse_factionnodespawninfo_entry(data, pos):
    """Auto-generated parser for factionnodespawninfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_4'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_5'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_6'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_7'] = struct.unpack_from('<f', data, pos)[0]; pos += 4

    return entry, pos
