#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title split
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "text" }
# @raycast.argument2 { "type": "text", "placeholder": "char", "optional": true}

# Documentation:
# @raycast.description 根据指定字符分割字符串
# @raycast.author luzhengli
# @raycast.authorURL https://raycast.com/luzhengli

import sys
s = sys.argv[1] 
split_str = sys.argv[2] 
if split_str == "":
    split_str = ','
ls = s.split(split_str)
for s in ls:
    print(s)


print('\n----------------------')
print('cnt: ', len(ls))