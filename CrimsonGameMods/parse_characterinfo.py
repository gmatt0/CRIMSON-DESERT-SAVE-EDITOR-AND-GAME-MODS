import struct

def parse_characterinfo_entry(data, pos):
    """Auto-generated parser for characterinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = data[pos]; pos += 1
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_4'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_5'] = data[pos]; pos += 1
    entry['field_6'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_7'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_8'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_9'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_10'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_11'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_12'] = data[pos]; pos += 1
    entry['field_13'] = data[pos]; pos += 1
    entry['field_14'] = data[pos]; pos += 1
    entry['field_15'] = data[pos]; pos += 1
    entry['field_16'] = data[pos]; pos += 1
    entry['field_17'] = data[pos]; pos += 1
    entry['field_18'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
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
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_33'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_34'] = data[pos]; pos += 1
    entry['field_35'] = data[pos]; pos += 1
    entry['field_36'] = data[pos]; pos += 1
    entry['field_37'] = data[pos]; pos += 1
    entry['field_38'] = data[pos]; pos += 1
    entry['field_39'] = data[pos]; pos += 1
    entry['field_40'] = data[pos]; pos += 1
    entry['field_41'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_42'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_43'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_44'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_45'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_46'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_47'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_48'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_49'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_50'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_51'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_52'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_53'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_54'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_55'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_56'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_57'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_58'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_59'] = data[pos]; pos += 1
    entry['field_60'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_61'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['field_62'] = data[pos]; pos += 1
    entry['field_63'] = data[pos]; pos += 1
    entry['field_64'] = data[pos]; pos += 1
    entry['field_65'] = data[pos]; pos += 1
    entry['field_66'] = data[pos]; pos += 1
    entry['field_67'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_68'] = data[pos]; pos += 1
    entry['field_69'] = data[pos]; pos += 1
    entry['field_70'] = data[pos]; pos += 1
    entry['field_71'] = data[pos]; pos += 1
    entry['field_72'] = data[pos]; pos += 1
    entry['field_73'] = data[pos]; pos += 1
    entry['field_74'] = data[pos]; pos += 1
    entry['field_75'] = data[pos]; pos += 1
    entry['field_76'] = data[pos]; pos += 1
    entry['field_77'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_78'] = data[pos]; pos += 1
    entry['field_79'] = data[pos]; pos += 1
    entry['field_80'] = data[pos]; pos += 1
    entry['field_81'] = data[pos]; pos += 1
    entry['field_82'] = data[pos]; pos += 1
    entry['field_83'] = data[pos]; pos += 1
    entry['field_84'] = data[pos]; pos += 1
    entry['field_85'] = data[pos]; pos += 1
    entry['field_86'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_87'] = data[pos]; pos += 1
    entry['field_88'] = data[pos]; pos += 1
    entry['field_89'] = data[pos]; pos += 1
    entry['field_90'] = data[pos]; pos += 1
    entry['field_91'] = data[pos]; pos += 1
    entry['field_92'] = data[pos]; pos += 1
    entry['field_93'] = data[pos]; pos += 1
    entry['field_94'] = data[pos]; pos += 1
    entry['field_95'] = data[pos]; pos += 1
    entry['field_96'] = data[pos]; pos += 1
    entry['field_97'] = data[pos]; pos += 1
    entry['field_98'] = data[pos]; pos += 1
    entry['field_99'] = data[pos]; pos += 1
    entry['field_100'] = data[pos]; pos += 1
    entry['field_101'] = data[pos]; pos += 1
    entry['field_102'] = data[pos]; pos += 1
    entry['field_103'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_104'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_105'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_106'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_107'] = data[pos]; pos += 1
    entry['field_108'] = data[pos]; pos += 1
    entry['field_109'] = data[pos]; pos += 1
    entry['field_110'] = data[pos]; pos += 1
    entry['field_111'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_112'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_113'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_114'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_115'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_116'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_117'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_118'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_119'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_120'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_121'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_122'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_123'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_124'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_125'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_126'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_127'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_128'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_129'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_130'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_131'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_132'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_133'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_134'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_135'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_136'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_137'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_138'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_139'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_140'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_141'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_142'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_143'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_144'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_145'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_146'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_147'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_148'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_149'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_150'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_151'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_152'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_153'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_154'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_155'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_156'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_157'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_158'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_159'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_160'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_161'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_162'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_163'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_164'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_165'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_166'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_167'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_168'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_169'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_170'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_171'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_172'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_173'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_174'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_175'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_176'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_177'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_178'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_179'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_180'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_181'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_182'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_183'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_184'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_185'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_186'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_187'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_188'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_189'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_190'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_191'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_192'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_193'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_194'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_195'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_196'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_197'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_198'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_199'] = struct.unpack_from('<f', data, pos)[0]; pos += 4

    return entry, pos
