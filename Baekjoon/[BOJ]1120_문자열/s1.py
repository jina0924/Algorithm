# 백준 1120번 문자열

import sys
sys.stdin = open('input.txt')

a, b = input().split()
la, lb = len(a), len(b)
maxV = 0
for i in range(lb - la + 1):
    cnt = 0
    for j in range(la):
        if a[j] == b[i + j]:
            cnt += 1
    maxV = max(maxV, cnt)
print(la - maxV)