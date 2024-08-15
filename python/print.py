#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title print
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description test print
# @raycast.author luzhengli
# @raycast.authorURL https://raycast.com/luzhengli


# 写一个函数帮我决定今天吃几号食堂，随机数总共可能有1-6（包含6）
import random

def decide_canteen():
    return random.randint(1, 6)

print(f'今天吃{decide_canteen()}食堂')