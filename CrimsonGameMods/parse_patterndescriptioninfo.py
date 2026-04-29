import struct

def parse_patterndescriptioninfo_entry(data, pos):
    """Auto-generated parser for patterndescriptioninfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_4'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_5'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_6'] = data[pos]; pos += 1
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_7'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_8'] = struct.unpack_from('<H', data, pos)[0]; pos += 2

    return entry, pos
