import struct

def parse_gimmickgateconnection_entry(data, pos):
    """Auto-generated parser for gimmickgateconnection entries."""
    entry = {}

    pos += 2  # padding
    pos += 2  # padding
    pos += 2  # padding
    pos += 2  # padding
    pos += 2  # padding
    pos += 2  # padding
    entry['field_6'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_7'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_8'] = data[pos]; pos += 1

    return entry, pos
