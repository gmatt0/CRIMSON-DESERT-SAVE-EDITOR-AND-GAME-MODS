import struct

def parse_allygroupinfo_entry(data, pos):
    """Auto-generated parser for allygroupinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_4'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_5'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_6'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_7'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_8'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_9'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_10'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_11'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_12'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_13'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_14'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_15'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_16'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_17'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_18'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_19'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_20'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_21'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_22'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_23'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_24'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_25'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_26'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_27'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_28'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_29'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_30'] = data[pos]; pos += 1

    return entry, pos
