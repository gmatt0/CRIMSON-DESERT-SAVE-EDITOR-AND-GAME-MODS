import struct

def parse_actionrestrictionorderinfo_entry(data, pos):
    """Auto-generated parser for actionrestrictionorderinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_3'] = data[pos]; pos += 1
    entry['field_4'] = data[pos]; pos += 1
    entry['field_5'] = data[pos]; pos += 1
    entry['field_6'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_7'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_8'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_9'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_10'] = data[pos]; pos += 1
    entry['field_11'] = data[pos]; pos += 1
    entry['field_12'] = data[pos]; pos += 1
    entry['field_13'] = data[pos]; pos += 1
    entry['field_14'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_15'] = data[pos]; pos += 1
    entry['field_16'] = data[pos]; pos += 1

    return entry, pos
