import struct

def parse_uisocialaction_entry(data, pos):
    """Auto-generated parser for uisocialaction entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_4'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_5'] = data[pos]; pos += 1
    entry['field_6'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_7'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_8'] = data[pos]; pos += 1
    entry['field_9'] = data[pos]; pos += 1

    return entry, pos
