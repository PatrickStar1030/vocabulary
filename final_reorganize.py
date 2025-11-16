# -*- coding: utf-8 -*-
"""
重组 forget.txt 文件：
1. 找出前90行中所有以!结尾的行
2. 移除!号，添加【遗忘】标记
3. 将这些行移到文件顶部
4. 保持其他行的顺序
"""
import re

with open('forget.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 处理前90行
forget_items = []
other_items = []

for i, line in enumerate(lines[:90]):
    # 去除行尾换行符，检查是否以!结尾
    stripped = line.rstrip('\n\r')
    if stripped and stripped.endswith('!'):
        # 移除末尾的!，添加【遗忘】标记
        cleaned = stripped[:-1].rstrip()  # 移除最后的!和可能的空格
        forget_items.append('【遗忘】' + cleaned + '\n')
    else:
        # 保留原行（包括换行符）
        other_items.append(line)

# 重组：遗忘词在前，其他词在后，然后是第91行及以后的内容
result = forget_items + other_items + lines[90:]

# 写入文件
with open('forget.txt', 'w', encoding='utf-8') as f:
    f.writelines(result)

print(f"已处理 {len(forget_items)} 个遗忘词，已移到顶部")
print(f"保留了 {len(other_items)} 个其他词")
print("文件已更新！")

