# 백준 1439번 뒤집기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

s = input().rstrip()
cnt = 0
char = s[0]
i = 0
while i < len(s):
    if s[i] != char:
        while i < len(s) and char != s[i]:
            i += 1
        cnt += 1
    i += 1
print(cnt)