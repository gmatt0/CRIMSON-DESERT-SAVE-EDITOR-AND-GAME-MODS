import struct

def parse_buffinfo_entry(data, pos):
    """Auto-generated parser for buffinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_2'] = data[pos]; pos += 1
    entry['field_3'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_4'] = data[pos]; pos += 1
    entry['field_5'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_6'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_7'] = data[pos]; pos += 1
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
    entry['field_21'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_22'] = data[pos]; pos += 1
    entry['field_23'] = data[pos]; pos += 1
    entry['field_24'] = data[pos]; pos += 1
    entry['field_25'] = data[pos]; pos += 1
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_26'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_27'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_28'] = data[pos]; pos += 1
    entry['field_29'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_30'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_31'] = data[pos]; pos += 1
    entry['field_32'] = data[pos]; pos += 1
    entry['field_33'] = data[pos]; pos += 1
    entry['field_34'] = data[pos]; pos += 1
    entry['field_35'] = data[pos]; pos += 1
    entry['field_36'] = data[pos]; pos += 1
    entry['field_37'] = data[pos]; pos += 1
    entry['field_38'] = data[pos]; pos += 1
    entry['field_39'] = data[pos]; pos += 1
    entry['field_40'] = data[pos]; pos += 1
    entry['field_41'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_42'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_43'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_44'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_45'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_46'] = data[pos]; pos += 1
    entry['field_47'] = data[pos]; pos += 1
    entry['field_48'] = data[pos]; pos += 1
    entry['field_49'] = data[pos]; pos += 1
    entry['field_50'] = data[pos]; pos += 1
    entry['field_51'] = data[pos]; pos += 1
    entry['field_52'] = data[pos]; pos += 1
    entry['field_53'] = data[pos]; pos += 1
    entry['field_54'] = data[pos]; pos += 1
    entry['field_55'] = data[pos]; pos += 1
    entry['field_56'] = data[pos]; pos += 1
    entry['field_57'] = data[pos]; pos += 1
    entry['field_58'] = data[pos]; pos += 1
    entry['field_59'] = data[pos]; pos += 1
    entry['field_60'] = data[pos]; pos += 1
    entry['field_61'] = data[pos]; pos += 1
    entry['field_62'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_63'] = data[pos]; pos += 1
    entry['field_64'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_65'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_66'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_67'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_68'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_69'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_70'] = data[pos]; pos += 1
    entry['field_71'] = data[pos]; pos += 1
    entry['field_72'] = data[pos]; pos += 1

    return entry, pos
