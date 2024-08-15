#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title strip
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "text" }
# @raycast.argument2 { "type": "text", "placeholder": "char", "optional": true}

# Documentation:⬇️
# @raycast.description 去除字符串两端制定的字符
# @raycast.author luzhengli
# @raycast.authorURL https://raycast.com/luzhengli

import sys

text = sys.argv[1] # 带格式化的字符串 如果是空格分割表示多个字符串
char = sys.argv[2] # 需要去除的字符

if char == '':
    for tet in text.split():
        print(text.strip())
else: 
    for tet in text.split():
        print(tet.strip(char))

