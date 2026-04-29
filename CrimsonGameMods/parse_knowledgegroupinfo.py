import struct

def parse_knowledgegroupinfo_entry(data, pos):
    """Auto-generated parser for knowledgegroupinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_4'] = data[pos]; pos += 1
    entry['field_5'] = data[pos]; pos += 1
    entry['field_6'] = data[pos]; pos += 1
    entry['field_7'] = data[pos]; pos += 1
    entry['field_8'] = data[pos]; pos += 1
    entry['field_9'] = data[pos]; pos += 1
    entry['field_10'] = data[pos]; pos += 1
    entry['field_11'] = data[pos]; pos += 1
    entry['field_12'] = data[pos]; pos += 1
    entry['field_13'] = data[pos]; pos += 1
    entry['field_14'] = data[pos]; pos += 1
    entry['field_15'] = data[pos]; pos += 1
    entry['field_16'] = data[pos]; pos += 1
    entry['field_17'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_18'] = data[pos]; pos += 1
    entry['field_19'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_20'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_21'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_22'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_23'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_24'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_25'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_26'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_27'] = struct.unpack_from('<H', data, pos)[0]; pos += 2
    entry['field_28'] = data[pos]; pos += 1

    return entry, pos
