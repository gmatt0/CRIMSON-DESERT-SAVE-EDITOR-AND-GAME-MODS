import struct

def parse_actionpointinfo_entry(data, pos):
    """Auto-generated parser for actionpointinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = data[pos]; pos += 1
    entry['field_3'] = data[pos]; pos += 1
    entry['field_4'] = data[pos]; pos += 1
    entry['field_5'] = data[pos]; pos += 1
    entry['field_6'] = data[pos]; pos += 1
    entry['field_7'] = data[pos]; pos += 1
    entry['field_8'] = data[pos]; pos += 1
    entry['field_9'] = data[pos]; pos += 1
    entry['field_10'] = data[pos]; pos += 1
    entry['field_11'] = data[pos]; pos += 1
    entry['field_12'] = data[pos]; pos += 1
    entry['field_13'] = data[pos]; pos += 1
    entry['field_14'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_15'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_16'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_17'] = data[pos]; pos += 1
    entry['field_18'] = data[pos]; pos += 1
    entry['field_19'] = data[pos]; pos += 1
    entry['field_20'] = data[pos]; pos += 1
    entry['field_21'] = data[pos]; pos += 1
    entry['field_22'] = data[pos]; pos += 1
    entry['field_23'] = data[pos]; pos += 1
    entry['field_24'] = data[pos]; pos += 1
    entry['field_25'] = data[pos]; pos += 1
    entry['field_26'] = data[pos]; pos += 1
    entry['field_27'] = data[pos]; pos += 1
    entry['field_28'] = data[pos]; pos += 1
    entry['field_29'] = data[pos]; pos += 1
    entry['field_30'] = data[pos]; pos += 1
    entry['field_31'] = data[pos]; pos += 1
    entry['field_32'] = data[pos]; pos += 1
    entry['field_33'] = data[pos]; pos += 1
    entry['field_34'] = data[pos]; pos += 1
    entry['field_35'] = data[pos]; pos += 1
    entry['field_36'] = data[pos]; pos += 1
    entry['field_37'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_38'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_39'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_40'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_41'] = data[pos]; pos += 1
    entry['field_42'] = data[pos]; pos += 1
    entry['field_43'] = data[pos]; pos += 1
    entry['field_44'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_45'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_46'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_47'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_48'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_49'] = data[pos]; pos += 1
    entry['field_50'] = data[pos]; pos += 1
    entry['field_51'] = data[pos]; pos += 1
    entry['field_52'] = data[pos]; pos += 1

    return entry, pos
