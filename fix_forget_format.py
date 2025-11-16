# -*- coding: utf-8 -*-
"""
修复 forget.txt 文件格式：
将第一行中所有连在一起的【遗忘】词分开，每个词一行
"""

with open('forget.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 处理第一行：按【遗忘】分割
if lines and lines[0].startswith('【遗忘】'):
    first_line = lines[0].rstrip('\n\r')
    # 按【遗忘】分割，保留分隔符
    parts = first_line.split('【遗忘】')
    
    # 重新组合：每个【遗忘】词一行（跳过第一个空字符串）
    fixed_forget_items = []
    for part in parts[1:]:  # 跳过第一个空字符串
        if part.strip():  # 只处理非空部分
            fixed_forget_items.append('【遗忘】' + part + '\n')
    
    # 重组文件：修复后的遗忘词 + 其他行
    result = fixed_forget_items + lines[1:]
else:
    result = lines

# 写入文件
with open('forget.txt', 'w', encoding='utf-8') as f:
    f.writelines(result)

print(f"已修复 {len(fixed_forget_items) if lines and lines[0].startswith('【遗忘】') else 0} 个遗忘词的格式")
print("文件已更新！")

