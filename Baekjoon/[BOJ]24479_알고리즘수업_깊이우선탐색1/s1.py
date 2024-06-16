# 백준 24479번 알고리줌 수업 - 깊이 우선 탐색1

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10 ** 5 + 1)


def dfs(c):
    global cnt
    for nc in data[c]:
        if not visited[nc]:
            cnt += 1
            visited[nc] = cnt
            dfs(nc)
    return


n, m, r = map(int, input().split())
data = defaultdict(list)
visited = [0] * (n + 1)
visited[r] = 1
cnt = 1
for _ in range(m):
    u, v = map(int, input().split())
    data[u].append(v)
    data[v].append(u)

for key in data.keys():
    data[key].sort()

dfs(r)

for i in range(1, n + 1):
    print(visited[i])