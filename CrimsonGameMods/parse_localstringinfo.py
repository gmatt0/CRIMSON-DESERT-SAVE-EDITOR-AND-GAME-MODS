import struct

def parse_localstringinfo_entry(data, pos):
    """Auto-generated parser for localstringinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_4'] = data[pos]; pos += 1

    return entry, pos
