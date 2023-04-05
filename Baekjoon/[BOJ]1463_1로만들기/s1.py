# 백준 1463번 1로 만들기 - 시간초과

import sys
sys.stdin = open('input.txt')
import heapq

X = int(input())
nums = [(0, X)]
while nums:
    cnt, num = heapq.heappop(nums)
    if num == 1:
        print(cnt)
        sys.exit()
    if num % 3 == 0:
        heapq.heappush(nums, (cnt + 1, num // 3))
    if num % 2 == 0:
        heapq.heappush(nums, (cnt + 1, num // 2))
    heapq.heappush(nums, (cnt + 1, num - 1))