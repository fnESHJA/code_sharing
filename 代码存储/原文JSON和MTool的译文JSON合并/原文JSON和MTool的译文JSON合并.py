import json
import re

def split_mixed_string(s):
    """
    将包含ASCII和非ASCII字符的字符串分割成多个子字符串，每个子字符串要么全为ASCII字符要么全不为ASCII字符。
    """
    return re.findall(r'[^\x00-\x7F]+|[\x00-\x7F]+', s)

def replace_non_ascii_segments(segments, trans_dic):
    """
    对分割后的字符串进行替换，将所有非ASCII字符串用trans_dic中的对应值替换。
    """
    result_segments = []
    for segment in segments:
        if all(ord(char) < 128 for char in segment):
            result_segments.append(segment)
        else:
            result_segments.append(trans_dic.get(segment, segment))
    return ''.join(result_segments)

def main():
    # 读取json1和json2
    with open('TrsData.json', 'r', encoding='utf-8') as f:
        trans_dic = json.load(f)
    
    with open('transDic.output.json', 'r', encoding='utf-8') as f:
        output_dic = json.load(f)
    
    # 处理json2的键
    new_output_dic = {}
    for key, value in output_dic.items():
        segments = split_mixed_string(key)
        new_key = replace_non_ascii_segments(segments, trans_dic)
        new_output_dic[key] = new_key
    
    # 将结果保存到transDic.output2.json
    with open('transDic.json', 'w', encoding='utf-8') as f:
        json.dump(new_output_dic, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
