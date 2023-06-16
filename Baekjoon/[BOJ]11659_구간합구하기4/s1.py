# 백준 11659번 구간 합 구하기4

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
for idx in range(N - 1):
    nums[idx + 1] += nums[idx]
for _ in range(M):
    i, j = map(int, input().split())
    if i > 1:
        print(nums[j - 1] - nums[i - 2])
    else:
        print(nums[j - 1])