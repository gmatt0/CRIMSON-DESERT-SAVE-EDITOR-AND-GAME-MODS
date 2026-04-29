import struct

def parse_effectinfo_entry(data, pos):
    """Auto-generated parser for effectinfo entries."""
    entry = {}

    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_0'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_1'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_3'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_4'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_5'] = data[pos]; pos += 1
    entry['field_6'] = data[pos]; pos += 1
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
    entry['field_62'] = data[pos]; pos += 1
    entry['field_63'] = data[pos]; pos += 1
    entry['field_64'] = data[pos]; pos += 1
    entry['field_65'] = data[pos]; pos += 1
    entry['field_66'] = data[pos]; pos += 1
    entry['field_67'] = data[pos]; pos += 1
    entry['field_68'] = data[pos]; pos += 1
    entry['field_69'] = data[pos]; pos += 1
    entry['field_70'] = data[pos]; pos += 1
    entry['field_71'] = data[pos]; pos += 1
    entry['field_72'] = data[pos]; pos += 1
    entry['field_73'] = data[pos]; pos += 1
    entry['field_74'] = data[pos]; pos += 1
    entry['field_75'] = data[pos]; pos += 1
    entry['field_76'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_77'] = data[pos]; pos += 1
    entry['field_78'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_79'] = data[pos]; pos += 1
    entry['field_80'] = data[pos]; pos += 1
    entry['field_81'] = data[pos]; pos += 1
    entry['field_82'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_83'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_84'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_85'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_86'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_87'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_88'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_89'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_90'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_91'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_92'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_93'] = data[pos]; pos += 1
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_94'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_95'] = data[pos]; pos += 1
    entry['field_96'] = data[pos]; pos += 1
    entry['field_97'] = data[pos]; pos += 1
    entry['field_98'] = data[pos]; pos += 1
    entry['field_99'] = data[pos]; pos += 1
    entry['field_100'] = data[pos]; pos += 1
    entry['field_101'] = data[pos]; pos += 1
    entry['field_102'] = data[pos]; pos += 1
    entry['field_103'] = data[pos]; pos += 1
    entry['field_104'] = data[pos]; pos += 1
    entry['field_105'] = data[pos]; pos += 1
    entry['field_106'] = data[pos]; pos += 1
    entry['field_107'] = data[pos]; pos += 1
    entry['field_108'] = data[pos]; pos += 1
    entry['field_109'] = data[pos]; pos += 1
    entry['field_110'] = data[pos]; pos += 1
    entry['field_111'] = data[pos]; pos += 1
    entry['field_112'] = data[pos]; pos += 1
    entry['field_113'] = data[pos]; pos += 1
    entry['field_114'] = data[pos]; pos += 1
    entry['field_115'] = data[pos]; pos += 1
    entry['field_116'] = data[pos]; pos += 1
    entry['field_117'] = data[pos]; pos += 1
    entry['field_118'] = data[pos]; pos += 1
    entry['field_119'] = data[pos]; pos += 1
    entry['field_120'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_121'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_122'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_123'] = data[pos]; pos += 1
    entry['field_124'] = data[pos]; pos += 1
    entry['field_125'] = data[pos]; pos += 1
    entry['field_126'] = data[pos]; pos += 1
    entry['field_127'] = data[pos]; pos += 1
    entry['field_128'] = data[pos]; pos += 1
    entry['field_129'] = data[pos]; pos += 1
    entry['field_130'] = data[pos]; pos += 1
    entry['field_131'] = data[pos]; pos += 1
    entry['field_132'] = data[pos]; pos += 1
    entry['field_133'] = data[pos]; pos += 1
    entry['field_134'] = data[pos]; pos += 1
    entry['field_135'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_136'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_137'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_138'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_139'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_140'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_141'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_142'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_143'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_144'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_145'] = data[pos]; pos += 1
    entry['field_146'] = data[pos]; pos += 1
    entry['field_147'] = data[pos]; pos += 1
    entry['field_148'] = data[pos]; pos += 1
    entry['field_149'] = data[pos]; pos += 1
    entry['field_150'] = data[pos]; pos += 1
    entry['field_151'] = data[pos]; pos += 1
    entry['field_152'] = data[pos]; pos += 1
    entry['field_153'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_154'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_155'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_156'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_157'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_158'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_159'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_160'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_161'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_162'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_163'] = data[pos]; pos += 1
    entry['field_164'] = data[pos]; pos += 1
    entry['field_165'] = data[pos]; pos += 1
    entry['field_166'] = data[pos]; pos += 1
    entry['field_167'] = data[pos]; pos += 1
    entry['field_168'] = data[pos]; pos += 1
    entry['field_169'] = data[pos]; pos += 1
    entry['field_170'] = data[pos]; pos += 1
    entry['field_171'] = data[pos]; pos += 1
    entry['field_172'] = data[pos]; pos += 1
    entry['field_173'] = data[pos]; pos += 1
    entry['field_174'] = data[pos]; pos += 1
    entry['field_175'] = data[pos]; pos += 1
    entry['field_176'] = data[pos]; pos += 1
    entry['field_177'] = data[pos]; pos += 1
    entry['field_178'] = data[pos]; pos += 1
    entry['field_179'] = data[pos]; pos += 1
    entry['field_180'] = data[pos]; pos += 1
    entry['field_181'] = data[pos]; pos += 1
    entry['field_182'] = data[pos]; pos += 1
    entry['field_183'] = data[pos]; pos += 1
    entry['field_184'] = data[pos]; pos += 1
    entry['field_185'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_186'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_187'] = data[pos]; pos += 1
    entry['field_188'] = data[pos]; pos += 1

    return entry, pos
