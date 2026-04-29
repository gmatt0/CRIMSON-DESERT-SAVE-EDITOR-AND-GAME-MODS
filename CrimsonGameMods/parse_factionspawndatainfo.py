import struct

def parse_factionspawndatainfo_entry(data, pos):
    """Auto-generated parser for factionspawndatainfo entries."""
    entry = {}

    entry['field_0'] = data[pos]; pos += 1
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = data[pos]; pos += 1
    entry['field_3'] = data[pos]; pos += 1
    entry['field_4'] = data[pos]; pos += 1
    entry['field_5'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_6'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_7'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_8'] = struct.unpack_from('<i', data, pos)[0]; pos += 4

    return entry, pos
