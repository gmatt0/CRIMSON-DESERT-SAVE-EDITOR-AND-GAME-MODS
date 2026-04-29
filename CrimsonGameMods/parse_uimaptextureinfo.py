import struct

def parse_uimaptextureinfo_entry(data, pos):
    """Auto-generated parser for uimaptextureinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_3'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_4'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_5'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_6'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_7'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_8'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_9'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_10'] = data[pos]; pos += 1
    entry['field_11'] = data[pos]; pos += 1
    entry['field_12'] = data[pos]; pos += 1
    entry['field_13'] = data[pos]; pos += 1
    entry['field_14'] = data[pos]; pos += 1
    entry['field_15'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_16'] = data[pos]; pos += 1
    entry['field_17'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_18'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_19'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_20'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_21'] = data[pos]; pos += 1
    entry['field_22'] = data[pos]; pos += 1
    entry['field_23'] = data[pos]; pos += 1
    entry['field_24'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_25'] = data[pos]; pos += 1
    entry['field_26'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_27'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_28'] = data[pos]; pos += 1
    entry['field_29'] = data[pos]; pos += 1
    entry['field_30'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_31'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_32'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_33'] = data[pos]; pos += 1
    entry['field_34'] = data[pos]; pos += 1
    entry['field_35'] = data[pos]; pos += 1
    entry['field_36'] = data[pos]; pos += 1
    entry['field_37'] = data[pos]; pos += 1
    entry['field_38'] = data[pos]; pos += 1
    entry['field_39'] = data[pos]; pos += 1
    entry['field_40'] = data[pos]; pos += 1
    entry['field_41'] = data[pos]; pos += 1
    entry['field_42'] = data[pos]; pos += 1
    entry['field_43'] = data[pos]; pos += 1
    entry['field_44'] = data[pos]; pos += 1
    entry['field_45'] = data[pos]; pos += 1
    entry['field_46'] = data[pos]; pos += 1
    entry['field_47'] = data[pos]; pos += 1
    entry['field_48'] = data[pos]; pos += 1
    entry['field_49'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
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
    entry['field_62'] = data[pos]; pos += 1
    entry['field_63'] = data[pos]; pos += 1
    entry['field_64'] = data[pos]; pos += 1
    entry['field_65'] = data[pos]; pos += 1
    entry['field_66'] = data[pos]; pos += 1
    entry['field_67'] = data[pos]; pos += 1
    entry['field_68'] = data[pos]; pos += 1
    entry['field_69'] = data[pos]; pos += 1

    return entry, pos
