#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title value_counts
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Placeholder" }

# Documentation:
# @raycast.description 统计每个元素出现的次数
# @raycast.author luzhengli
# @raycast.authorURL https://raycast.com/luzhengli

import sys
# print("Hello World! Argument1 value: " + sys.argv[1])
elements = sys.argv[1]

# 统计每个元素出现的次数
from collections import Counter
elements = elements.split()
result = Counter(elements)

# 以命令行输出的形式展示结果
print("|元素|出现次数|")
print("------------")
for key, value in result.items():
    print(f"{key} {value}")
