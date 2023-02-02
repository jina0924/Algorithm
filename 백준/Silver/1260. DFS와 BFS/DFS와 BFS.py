# 백준 1260번 DFS와 BFS

import sys
input = sys.stdin.readline
from collections import deque


def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)


def bfs(v):
    queue = deque([v])
    visited = [0] * (N + 1)
    visited[v] = 1

    while queue:
        cv = queue.popleft()
        print(cv, end=' ')
        for nv in graph[cv]:
            if not visited[nv]:
                queue.append(nv)
                visited[nv] = 1


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for g in graph:
    g.sort()
visited = [0] * (N + 1)
dfs(V)
print()
bfs(V)
