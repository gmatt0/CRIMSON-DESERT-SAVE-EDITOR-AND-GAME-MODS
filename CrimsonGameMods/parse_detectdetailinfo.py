import struct

def parse_detectdetailinfo_entry(data, pos):
    """Auto-generated parser for detectdetailinfo entries."""
    entry = {}

    entry['field_0'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_1'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_2'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_3'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_4'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_5'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_6'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_7'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_8'] = data[pos]; pos += 1
    entry['field_9'] = data[pos]; pos += 1
    entry['field_10'] = data[pos]; pos += 1
    entry['field_11'] = data[pos]; pos += 1
    entry['field_12'] = data[pos]; pos += 1
    entry['field_13'] = data[pos]; pos += 1
    entry['field_14'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_15'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_16'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_17'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_18'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_19'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_20'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_21'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_22'] = data[pos]; pos += 1
    entry['field_23'] = data[pos]; pos += 1
    entry['field_24'] = data[pos]; pos += 1
    entry['field_25'] = data[pos]; pos += 1
    entry['field_26'] = data[pos]; pos += 1
    entry['field_27'] = data[pos]; pos += 1
    entry['field_28'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_29'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_30'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_31'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_32'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_33'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_34'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_35'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_36'] = data[pos]; pos += 1
    entry['field_37'] = data[pos]; pos += 1
    entry['field_38'] = data[pos]; pos += 1
    entry['field_39'] = data[pos]; pos += 1
    entry['field_40'] = data[pos]; pos += 1
    entry['field_41'] = data[pos]; pos += 1
    entry['field_42'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_43'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_44'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_45'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_46'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_47'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_48'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_49'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_50'] = data[pos]; pos += 1
    entry['field_51'] = data[pos]; pos += 1
    entry['field_52'] = data[pos]; pos += 1
    entry['field_53'] = data[pos]; pos += 1
    entry['field_54'] = data[pos]; pos += 1
    entry['field_55'] = data[pos]; pos += 1
    entry['field_56'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_57'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_58'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_59'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_60'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_61'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_62'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_63'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_64'] = data[pos]; pos += 1
    entry['field_65'] = data[pos]; pos += 1
    entry['field_66'] = data[pos]; pos += 1
    entry['field_67'] = data[pos]; pos += 1
    entry['field_68'] = data[pos]; pos += 1
    entry['field_69'] = data[pos]; pos += 1
    entry['field_70'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_71'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_72'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_73'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_74'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_75'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_76'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_77'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_78'] = data[pos]; pos += 1
    entry['field_79'] = data[pos]; pos += 1
    entry['field_80'] = data[pos]; pos += 1
    entry['field_81'] = data[pos]; pos += 1
    entry['field_82'] = data[pos]; pos += 1
    entry['field_83'] = data[pos]; pos += 1
    entry['field_84'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_85'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_86'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_87'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_88'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_89'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_90'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_91'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_92'] = data[pos]; pos += 1
    entry['field_93'] = data[pos]; pos += 1
    entry['field_94'] = data[pos]; pos += 1
    entry['field_95'] = data[pos]; pos += 1
    entry['field_96'] = data[pos]; pos += 1
    entry['field_97'] = data[pos]; pos += 1
    entry['field_98'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_99'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_100'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_101'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_102'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_103'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_104'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_105'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_106'] = data[pos]; pos += 1
    entry['field_107'] = data[pos]; pos += 1
    entry['field_108'] = data[pos]; pos += 1
    entry['field_109'] = data[pos]; pos += 1
    entry['field_110'] = data[pos]; pos += 1
    entry['field_111'] = data[pos]; pos += 1
    entry['field_112'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_113'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_114'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_115'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_116'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_117'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_118'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_119'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_120'] = data[pos]; pos += 1
    entry['field_121'] = data[pos]; pos += 1
    entry['field_122'] = data[pos]; pos += 1
    entry['field_123'] = data[pos]; pos += 1
    entry['field_124'] = data[pos]; pos += 1
    entry['field_125'] = data[pos]; pos += 1
    entry['field_126'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_127'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_128'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_129'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_130'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_131'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_132'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_133'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_134'] = data[pos]; pos += 1
    entry['field_135'] = data[pos]; pos += 1
    entry['field_136'] = data[pos]; pos += 1
    entry['field_137'] = data[pos]; pos += 1
    entry['field_138'] = data[pos]; pos += 1
    entry['field_139'] = data[pos]; pos += 1
    entry['field_140'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_141'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_142'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_143'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_144'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_145'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_146'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_147'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_148'] = data[pos]; pos += 1
    entry['field_149'] = data[pos]; pos += 1
    entry['field_150'] = data[pos]; pos += 1
    entry['field_151'] = data[pos]; pos += 1
    entry['field_152'] = data[pos]; pos += 1
    entry['field_153'] = data[pos]; pos += 1
    entry['field_154'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_155'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_156'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_157'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_158'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_159'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_160'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_161'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_162'] = data[pos]; pos += 1
    entry['field_163'] = data[pos]; pos += 1
    entry['field_164'] = data[pos]; pos += 1
    entry['field_165'] = data[pos]; pos += 1
    entry['field_166'] = data[pos]; pos += 1
    entry['field_167'] = data[pos]; pos += 1
    entry['field_168'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_169'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_170'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_171'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_172'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_173'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_174'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_175'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_176'] = data[pos]; pos += 1
    entry['field_177'] = data[pos]; pos += 1
    entry['field_178'] = data[pos]; pos += 1
    entry['field_179'] = data[pos]; pos += 1
    entry['field_180'] = data[pos]; pos += 1
    entry['field_181'] = data[pos]; pos += 1
    entry['field_182'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_183'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_184'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_185'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_186'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_187'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_188'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_189'] = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['field_190'] = data[pos]; pos += 1
    entry['field_191'] = data[pos]; pos += 1
    entry['field_192'] = data[pos]; pos += 1
    entry['field_193'] = data[pos]; pos += 1
    entry['field_194'] = data[pos]; pos += 1
    entry['field_195'] = data[pos]; pos += 1
    entry['field_196'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_197'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_198'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['field_199'] = struct.unpack_from('<f', data, pos)[0]; pos += 4

    return entry, pos
