import struct

def parse_gameadvicegroupinfo_entry(data, pos):
    """Auto-generated parser for gameadvicegroupinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_4'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_5'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_6'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_7'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_8'] = data[pos]; pos += 1
    entry['field_9'] = data[pos]; pos += 1
    entry['field_10'] = data[pos]; pos += 1
    entry['field_11'] = data[pos]; pos += 1
    entry['field_12'] = data[pos]; pos += 1
    entry['field_13'] = data[pos]; pos += 1
    entry['field_14'] = data[pos]; pos += 1
    entry['field_15'] = data[pos]; pos += 1
    entry['field_16'] = data[pos]; pos += 1
    entry['field_17'] = data[pos]; pos += 1
    entry['field_18'] = data[pos]; pos += 1
    entry['field_19'] = data[pos]; pos += 1
    entry['field_20'] = data[pos]; pos += 1
    entry['field_21'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_22'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_23'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_24'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_25'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_26'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_27'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_28'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_29'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_30'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_31'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_32'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_33'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_34'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_35'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_36'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_37'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_38'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_39'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_40'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_41'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_42'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_43'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_44'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_45'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_46'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_47'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_48'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_49'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_50'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_51'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_52'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_53'] = struct.unpack_from('<i', data, pos)[0]; pos += 4

    return entry, pos
