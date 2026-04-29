import struct

def parse_socketgroupinfo_entry(data, pos):
    """Auto-generated parser for socketgroupinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_3'] = data[pos]; pos += 1

    return entry, pos
