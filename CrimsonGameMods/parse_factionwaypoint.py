import struct

def parse_factionwaypoint_entry(data, pos):
    """Auto-generated parser for factionwaypoint entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<f', data, pos)[0]; pos += 4

    return entry, pos
