import struct

def parse_statusinfo_entry(data, pos):
    """Auto-generated parser for statusinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = data[pos]; pos += 1
    entry['field_3'] = data[pos]; pos += 1
    entry['field_4'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_5'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_6'] = data[pos]; pos += 1
    entry['field_7'] = data[pos]; pos += 1
    entry['field_8'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_9'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_10'] = data[pos]; pos += 1
    entry['field_11'] = data[pos]; pos += 1
    entry['field_12'] = data[pos]; pos += 1
    entry['field_13'] = data[pos]; pos += 1
    entry['field_14'] = data[pos]; pos += 1
    entry['field_15'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_16'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_17'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_18'] = data[pos]; pos += 1
    entry['field_19'] = data[pos]; pos += 1
    entry['field_20'] = data[pos]; pos += 1
    entry['field_21'] = data[pos]; pos += 1
    entry['field_22'] = data[pos]; pos += 1
    entry['field_23'] = data[pos]; pos += 1
    entry['field_24'] = data[pos]; pos += 1
    entry['field_25'] = data[pos]; pos += 1
    entry['field_26'] = data[pos]; pos += 1
    entry['field_27'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_28'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_29'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_30'] = data[pos]; pos += 1
    entry['field_31'] = data[pos]; pos += 1
    entry['field_32'] = data[pos]; pos += 1
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_33'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_34'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_35'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_36'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_37'] = data[pos]; pos += 1

    return entry, pos
