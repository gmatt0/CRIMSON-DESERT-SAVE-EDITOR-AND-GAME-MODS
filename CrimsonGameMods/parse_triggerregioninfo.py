import struct

def parse_triggerregioninfo_entry(data, pos):
    """Auto-generated parser for triggerregioninfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_4'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_5'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_6'] = data[pos]; pos += 1
    entry['field_7'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_8'] = data[pos]; pos += 1
    entry['field_9'] = data[pos]; pos += 1
    entry['field_10'] = data[pos]; pos += 1
    entry['field_11'] = data[pos]; pos += 1
    entry['field_12'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_13'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_14'] = data[pos]; pos += 1
    entry['field_15'] = data[pos]; pos += 1
    entry['field_16'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_17'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_18'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_19'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_20'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_21'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_22'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_23'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_24'] = data[pos]; pos += 1
    entry['field_25'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_26'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_27'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_28'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_29'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_30'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_31'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_32'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_33'] = data[pos]; pos += 1
    entry['field_34'] = data[pos]; pos += 1
    entry['field_35'] = data[pos]; pos += 1
    entry['field_36'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_37'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_38'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_39'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_40'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_41'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_42'] = data[pos]; pos += 1
    entry['field_43'] = data[pos]; pos += 1

    return entry, pos
