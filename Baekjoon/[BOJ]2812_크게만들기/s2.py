# 백준 2812번 크게 만들기

import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
num = list(map(int, input()))
start, si = num[0], 0
for i in range(1, N):
    if num[i] > start:
        si = i
        start = num[i]
    if i >= K:
        break
K -= si
tmp = [start]
while K and si < N - 1:
    si += 1
    if num[si] < num[si + 1]:
        K -= 1
    else:
        tmp.append(num[si])
for i in range(si + 1, N):
    tmp.append(num[i])
ans = 0
ten = 1
for j in range(len(tmp) - 1, -1, -1):
    ans += tmp[j] * ten
    ten *= 10
print(ans)