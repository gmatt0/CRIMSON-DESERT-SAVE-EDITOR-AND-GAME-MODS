import struct

def parse_gameplayvariableinfo_entry(data, pos):
    """Auto-generated parser for gameplayvariableinfo entries."""
    entry = {}

    entry['field_0'] = data[pos]; pos += 1
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen

    return entry, pos
