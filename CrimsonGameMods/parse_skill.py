import struct

def parse_skill_entry(data, pos):
    """Auto-generated parser for skill entries."""
    entry = {}

    entry['isBlocked'] = data[pos]; pos += 1
    entry['stringKey'] = data[pos]; pos += 1
    entry['needUpgradeItemInfo'] = data[pos]; pos += 1
    entry['needUpgradeItemCountGraph'] = data[pos]; pos += 1
    _slen = struct.unpack_from('<I', data, pos)[0]; pos += 4
    entry['needUpgradeExperienceGraph'] = data[pos:pos + _slen].decode('utf-8', errors='replace'); pos += _slen
    entry['usableCharacterInfoList'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['usableCondition'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['learnKnowledgeInfo'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['factionInfo'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['useResourceStatList'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['isBlocked'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['cooltime'] = struct.unpack_from('<f', data, pos)[0]; pos += 4
    entry['buffLevelList'] = data[pos]; pos += 1
    entry['skillGroupKey'] = data[pos]; pos += 1
    entry['parentSkill'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['learnLevel'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['applyType'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['iconPath'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['uiType'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['reserveSlotInfoList'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['maxLevel'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['skillGroupKeyList'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['buffSustainFlag'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['devSkillName'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['devSkillDesc'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['videoPath'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['useResourceItemList'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['useDriverResourceStatList'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['useBatteryStat'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['isUiUseAllowed'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['isLearnUseArtifact'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['allowSkillWithLowResource'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['isUseChildPatternDescriptionBuffData'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['damageType'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_34'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_35'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_36'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_37'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_38'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_39'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_40'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_41'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_42'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_43'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_44'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
    entry['field_45'] = struct.unpack_from('<i', data, pos)[0]; pos += 4
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
    entry['field_64'] = data[pos]; pos += 1
    entry['field_65'] = data[pos]; pos += 1

    return entry, pos
