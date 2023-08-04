# 백준 1654번 랜선 자르기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]
left, right = 1, max(cables)
ans = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for cable in cables:
        cnt += cable // mid
    if cnt < N:
        right = mid - 1
    elif cnt >= N:
        ans = mid
        left = mid + 1
print(ans)