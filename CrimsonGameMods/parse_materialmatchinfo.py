import struct

def parse_materialmatchinfo_entry(data, pos):
    """Auto-generated parser for materialmatchinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_4'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen

    return entry, pos
