import struct

def parse_aidialogtypeinfo_entry(data, pos):
    """Auto-generated parser for aidialogtypeinfo entries."""
    entry = {}

    entry['field_0'] = data[pos]; pos += 1
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_3'] = data[pos]; pos += 1

    return entry, pos
