import struct

def parse_gimmickgroupinfo_entry(data, pos):
    """Auto-generated parser for gimmickgroupinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = data[pos]; pos += 1
    entry['field_3'] = data[pos]; pos += 1
    entry['field_4'] = data[pos]; pos += 1
    entry['field_5'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_6'] = data[pos]; pos += 1
    entry['field_7'] = data[pos]; pos += 1
    entry['field_8'] = data[pos]; pos += 1
    entry['field_9'] = data[pos]; pos += 1
    entry['field_10'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_11'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_12'] = data[pos:pos + 28]; pos += 28  # struct(i64+i64+i64+u32)
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_13'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_14'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_15'] = data[pos]; pos += 1
    entry['field_16'] = data[pos:pos + 28]; pos += 28  # struct(i64+i64+i64+u32)
    entry['field_17'] = data[pos]; pos += 1
    entry['field_18'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_19'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_20'] = data[pos]; pos += 1
    entry['field_21'] = data[pos]; pos += 1
    entry['field_22'] = data[pos]; pos += 1
    entry['field_23'] = data[pos]; pos += 1
    entry['field_24'] = data[pos]; pos += 1
    entry['field_25'] = data[pos]; pos += 1
    entry['field_26'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_27'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_28'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_29'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_30'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_31'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_32'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_33'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_34'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_35'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_36'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_37'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_38'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_39'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_40'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_41'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_42'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_43'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_44'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_45'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_46'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_47'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_48'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_49'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_50'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_51'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_52'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_53'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_54'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_55'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_56'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_57'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_58'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_59'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_60'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_61'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_62'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_63'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_64'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_65'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_66'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_67'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_68'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_69'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_70'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_71'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_72'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_73'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_74'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_75'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_76'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_77'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_78'] = struct.unpack_from('<i', data, pos)[0]; pos += 4

    return entry, pos
