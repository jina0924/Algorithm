# 백준 1439번 뒤집기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

s = input().rstrip()
cnt = 1
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        cnt += 1
print(cnt // 2)