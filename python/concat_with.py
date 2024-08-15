#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title concat_with
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "text" }
# @raycast.argument2 { "type": "text", "placeholder": "char" }

# Documentation:
# @raycast.description 按照指定字符拼接字符串
# @raycast.author luzhengli
# @raycast.authorURL https://raycast.com/luzhengli

import sys
s = sys.argv[1]
c = sys.argv[2]

# 按照若干个空格(使用正则)拆分字符串
import re
s = re.split(r'\s+', s)
print(c.join(s))