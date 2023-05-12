import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)


def dfs(v, visited):
    if visited[v]:
        return
    visited[v] = 1
    if isStart:
        for nv in graph[v]:
            dfs(nv, visited)
    else:
        for nv in graphR[v]:
            dfs(nv, visited)


n, m = map(int, input().split())
graph = defaultdict(list)
graphR = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graphR[y].append(x)
s, t = map(int, input().split())
isStart = True
fromS = [0] * (n + 1)
fromS[t] = 1
dfs(s, fromS)

fromT = [0] * (n + 1)
fromT[s] = 1
dfs(t, fromT)

isStart = False
toS = [0] * (n + 1)
dfs(s, toS)

toT = [0] * (n + 1)
dfs(t, toT)

cnt = 0
for i in range(1, n + 1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        cnt += 1
print(fromS, fromT, toS, toT)
print(cnt - 2)