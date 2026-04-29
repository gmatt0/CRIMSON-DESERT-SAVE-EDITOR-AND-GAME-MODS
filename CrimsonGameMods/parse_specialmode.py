import struct

def parse_specialmode_entry(data, pos):
    """Auto-generated parser for specialmode entries."""
    entry = {}

    entry['field_0'] = data[pos]; pos += 1
    entry['field_1'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_2'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_3'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_4'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_5'] = data[pos]; pos += 1
    entry['field_6'] = data[pos]; pos += 1
    entry['field_7'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_8'] = data[pos]; pos += 1
    entry['field_9'] = data[pos]; pos += 1
    entry['field_10'] = data[pos]; pos += 1
    entry['field_11'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_12'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_13'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_14'] = data[pos]; pos += 1
    entry['field_15'] = data[pos]; pos += 1
    entry['field_16'] = data[pos]; pos += 1
    entry['field_17'] = data[pos]; pos += 1
    entry['field_18'] = data[pos]; pos += 1
    entry['field_19'] = data[pos]; pos += 1
    entry['field_20'] = data[pos]; pos += 1
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_21'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_22'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_23'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_24'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_25'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_26'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_27'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_28'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_29'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_30'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_31'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_32'] = data[pos]; pos += 1
    entry['field_33'] = data[pos]; pos += 1
    entry['field_34'] = data[pos]; pos += 1
    entry['field_35'] = data[pos]; pos += 1
    entry['field_36'] = data[pos]; pos += 1
    entry['field_37'] = data[pos]; pos += 1
    entry['field_38'] = data[pos]; pos += 1
    entry['field_39'] = data[pos]; pos += 1
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_40'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_41'] = data[pos]; pos += 1
    entry['field_42'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_43'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_44'] = data[pos]; pos += 1
    entry['field_45'] = data[pos]; pos += 1
    entry['field_46'] = data[pos]; pos += 1
    entry['field_47'] = data[pos]; pos += 1
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_48'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_49'] = data[pos]; pos += 1
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_50'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_51'] = data[pos]; pos += 1
    entry['field_52'] = data[pos]; pos += 1
    entry['field_53'] = data[pos]; pos += 1
    entry['field_54'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_55'] = data[pos]; pos += 1
    entry['field_56'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_57'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_58'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_59'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_60'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_61'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_62'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_63'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_64'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_65'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_66'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_67'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_68'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_69'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_70'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_71'] = data[pos]; pos += 1
    entry['field_72'] = data[pos]; pos += 1
    entry['field_73'] = data[pos]; pos += 1
    entry['field_74'] = data[pos]; pos += 1
    entry['field_75'] = data[pos]; pos += 1
    entry['field_76'] = data[pos]; pos += 1

    return entry, pos
