#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title qc_文本去重
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Placeholder" }

# Documentation:
# @raycast.author luzhengli
# @raycast.authorURL https://raycast.com/luzhengli

import sys
# print("Hello World! Argument1 value: " + sys.argv[1])
text = sys.argv[1]

# 请实现一个函数，输入是一行由若干空格分割的字符串（实际包含多个字符串），输出是去重后的多行字符串，每个字符串一行
# 例如：
# 输入：
# "123  123  12 12"
# 输出：
# """
# 123
# 12
# """
# 代码如下：
text = text.split()
text = list(set(text))
cnt = len(text)
print("\n".join(text))

print('\n-----------------------------------')
print(f"【不同的字符串个数】: {cnt}")