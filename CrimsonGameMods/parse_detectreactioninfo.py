import struct

def parse_detectreactioninfo_entry(data, pos):
    """Auto-generated parser for detectreactioninfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_3'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_4'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_5'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_6'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_7'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_8'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_9'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_10'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_11'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_12'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_13'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_14'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_15'] = data[pos]; pos += 1
    entry['field_16'] = data[pos]; pos += 1
    entry['field_17'] = data[pos]; pos += 1

    return entry, pos
