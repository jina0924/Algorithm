# 백준 13418번 학교 탐방하기

import sys
sys.stdin = open('input.txt')
import heapq


def dijkstra(flag):
    heap = [(0, 0)]
    visited = [0] * (n + 1)
    k = 0

    while heap:
        d, cv = heapq.heappop(heap)
        if visited[cv]:
            continue
        visited[cv] = 1
        if d == 2 or d == -2:
            k += 1
        for nv in range(n + 1):
            if graph[cv][nv] and not visited[nv]:
                if flag == 1:
                    heapq.heappush(heap, (graph[cv][nv], nv))
                else:
                    heapq.heappush(heap, (-graph[cv][nv], nv))
    return k ** 2


n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m + 1):
    a, b, c = map(int, input().split())
    if c == 0:
        graph[a][b] = graph[b][a] = 2
    else:
        graph[a][b] = graph[b][a] = 1
k = dijkstra(1)     # 최소힙
K = dijkstra(2)     # 최대힙
print(K - k)