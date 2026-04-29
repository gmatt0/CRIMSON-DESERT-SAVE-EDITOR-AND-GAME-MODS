import struct

def parse_aimovespeedinfo_entry(data, pos):
    """Auto-generated parser for aimovespeedinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_3'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_4'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_5'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_6'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_7'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_8'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_9'] = data[pos]; pos += 1
    entry['field_10'] = data[pos]; pos += 1
    entry['field_11'] = data[pos]; pos += 1
    entry['field_12'] = data[pos]; pos += 1
    entry['field_13'] = data[pos]; pos += 1
    entry['field_14'] = data[pos]; pos += 1
    entry['field_15'] = data[pos]; pos += 1
    entry['field_16'] = data[pos]; pos += 1
    entry['field_17'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_18'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_19'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_20'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_21'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_22'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_23'] = data[pos]; pos += 1
    entry['field_24'] = data[pos]; pos += 1
    entry['field_25'] = data[pos]; pos += 1
    entry['field_26'] = data[pos]; pos += 1
    entry['field_27'] = data[pos]; pos += 1
    entry['field_28'] = data[pos]; pos += 1
    entry['field_29'] = data[pos]; pos += 1
    entry['field_30'] = data[pos]; pos += 1
    entry['field_31'] = data[pos]; pos += 1
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
    entry['field_44'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_45'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_46'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_47'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_48'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_49'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_50'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_51'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_52'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_53'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_54'] = data[pos]; pos += 1
    entry['field_55'] = data[pos]; pos += 1
    entry['field_56'] = data[pos]; pos += 1
    entry['field_57'] = data[pos]; pos += 1
    entry['field_58'] = data[pos]; pos += 1
    entry['field_59'] = data[pos]; pos += 1
    entry['field_60'] = data[pos]; pos += 1
    entry['field_61'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_62'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_63'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_64'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_65'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_66'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_67'] = data[pos]; pos += 1
    entry['field_68'] = data[pos]; pos += 1
    entry['field_69'] = data[pos]; pos += 1
    entry['field_70'] = data[pos]; pos += 1
    entry['field_71'] = data[pos]; pos += 1
    entry['field_72'] = data[pos]; pos += 1
    entry['field_73'] = data[pos]; pos += 1
    entry['field_74'] = data[pos]; pos += 1
    entry['field_75'] = data[pos]; pos += 1
    entry['field_76'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_77'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_78'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_79'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_80'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_81'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_82'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_83'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_84'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_85'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_86'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_87'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_88'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_89'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_90'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_91'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_92'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_93'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_94'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_95'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_96'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_97'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_98'] = data[pos]; pos += 1
    entry['field_99'] = data[pos]; pos += 1
    entry['field_100'] = data[pos]; pos += 1
    entry['field_101'] = data[pos]; pos += 1
    entry['field_102'] = data[pos]; pos += 1
    entry['field_103'] = data[pos]; pos += 1
    entry['field_104'] = data[pos]; pos += 1
    entry['field_105'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_106'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_107'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_108'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_109'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_110'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_111'] = data[pos]; pos += 1
    entry['field_112'] = data[pos]; pos += 1
    entry['field_113'] = data[pos]; pos += 1
    entry['field_114'] = data[pos]; pos += 1
    entry['field_115'] = data[pos]; pos += 1
    entry['field_116'] = data[pos]; pos += 1
    entry['field_117'] = data[pos]; pos += 1
    entry['field_118'] = data[pos]; pos += 1
    entry['field_119'] = data[pos]; pos += 1
    entry['field_120'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_121'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_122'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_123'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_124'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_125'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_126'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_127'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_128'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_129'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_130'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_131'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_132'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_133'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_134'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_135'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_136'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_137'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_138'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_139'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_140'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_141'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_142'] = data[pos]; pos += 1
    entry['field_143'] = data[pos]; pos += 1
    entry['field_144'] = data[pos]; pos += 1
    entry['field_145'] = data[pos]; pos += 1
    entry['field_146'] = data[pos]; pos += 1
    entry['field_147'] = data[pos]; pos += 1
    entry['field_148'] = data[pos]; pos += 1
    entry['field_149'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_150'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_151'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_152'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_153'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_154'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_155'] = data[pos]; pos += 1
    entry['field_156'] = data[pos]; pos += 1
    entry['field_157'] = data[pos]; pos += 1
    entry['field_158'] = data[pos]; pos += 1
    entry['field_159'] = data[pos]; pos += 1
    entry['field_160'] = data[pos]; pos += 1
    entry['field_161'] = data[pos]; pos += 1
    entry['field_162'] = data[pos]; pos += 1
    entry['field_163'] = data[pos]; pos += 1
    entry['field_164'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_165'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_166'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_167'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_168'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_169'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_170'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_171'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_172'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_173'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_174'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_175'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_176'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_177'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_178'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_179'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_180'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_181'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_182'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_183'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_184'] = data[pos]; pos += 1
    entry['field_185'] = data[pos]; pos += 1
    entry['field_186'] = data[pos]; pos += 1
    entry['field_187'] = data[pos]; pos += 1
    entry['field_188'] = data[pos]; pos += 1
    entry['field_189'] = data[pos]; pos += 1
    entry['field_190'] = data[pos]; pos += 1
    entry['field_191'] = data[pos]; pos += 1
    entry['field_192'] = data[pos]; pos += 1
    entry['field_193'] = data[pos]; pos += 1
    entry['field_194'] = data[pos]; pos += 1
    entry['field_195'] = data[pos]; pos += 1
    entry['field_196'] = data[pos]; pos += 1
    entry['field_197'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_198'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_199'] = struct.unpack_from('<I', data, pos)[0]; pos += 4

    return entry, pos
