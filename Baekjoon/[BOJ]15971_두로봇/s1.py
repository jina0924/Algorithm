# 백준 15971번 두 로봇 - 46%

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict
import heapq


def connect():
    heap = [(0, A, 0), (0, B, 0)]
    visited = [0] * (N + 1)
    cnt = [-1] * (N + 1)
    cnt[A] = cnt[B] = 0
    visited[A], visited[B] = A, B

    while heap:
        cw, cv, cost = heapq.heappop(heap)
        cnt[cv] = cost
        visited[cv] = 1
        for nv, nw in graph[cv]:
            if not visited[nv]:
                heapq.heappush(heap, (nw, nv, cnt[cv] + nw))


N, A, B = map(int, input().split())
graph = defaultdict(list)
for _ in range(N - 1):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
    graph[y].append((x, w))
if A == B:
    print(0)
else:
    print(connect())