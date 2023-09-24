# 백준 2212번 센서

import sys
sys.stdin = open('input.txt')
import heapq

N = int(input())
K = int(input())
sensors = sorted((map(int, input().split())))

heap = []
for i in range(1, N):
    heapq.heappush(heap, sensors[i] - sensors[i - 1])

ans = 0
# 거리 가장 먼 (K - 1)개 빼면 최소거리값 나옴
for _ in range(N - K):
    ans += heapq.heappop(heap)

print(ans)