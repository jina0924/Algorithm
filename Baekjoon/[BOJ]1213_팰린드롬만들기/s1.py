# 백준 1213번 팰린드롬 만들기

import sys
sys.stdin = open('input.txt')
from collections import defaultdict

name = input()
data = defaultdict(int)
for char in name:
    data[char] += 1
data = dict(sorted(data.items()))

left, mid = '', ''
for alpha, cnt in data.items():
    if cnt % 2:
        if mid:
            print("I'm Sorry Hansoo")
            sys.exit()
        else:
            mid = alpha
            cnt -= 1
    for _ in range(cnt // 2):
        left += alpha
print(left + mid + left[::-1])