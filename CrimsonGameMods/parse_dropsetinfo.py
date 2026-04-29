import struct

def parse_dropsetinfo_entry(data, pos):
    """Auto-generated parser for dropsetinfo entries."""
    entry = {}

    _field_0_flag = data[pos]; pos += 1
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_0'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_0_flag'] = _field_0_flag
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = data[pos]; pos += 1
    entry['field_3'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_4'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_5'] = data[pos]; pos += 1
    entry['field_6'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_7'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_8'] = data[pos]; pos += 1
    entry['field_9'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_10'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_11'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_12'] = data[pos]; pos += 1

    return entry, pos
