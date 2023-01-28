# 백준 1238번 파티

import sys
input = sys.stdin.readline
import heapq


def dijkstra(s, dist, graph):
    heap = []
    heapq.heappush(heap, (0, s))
    dist[s] = 0

    while heap:
        t, node = heapq.heappop(heap)
        if dist[node] < t:
            continue
        for neighbor in graph[node]:
            cost = dist[node] + neighbor[1]
            if cost < dist[neighbor[0]]:
                dist[neighbor[0]] = cost
                heapq.heappush(heap, (cost, neighbor[0]))


N, M, X = map(int, input().split())
INF = int(1e9)
dist1 = [0] + [INF] * (N)
dist2 = [0] + [INF] * (N)
graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, t = map(int, input().split())
    graph1[start].append((end, t))
    graph2[end].append((start, t))

dijkstra(X, dist1, graph1)
dijkstra(X, dist2, graph2)

ans = 0
for i in range(1, N+1):
    ans = max(dist1[i] + dist2[i], ans)

print(ans)