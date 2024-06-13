# 백준 24444번 알고리즘 수업 - 너비 우선 탐색1

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque, defaultdict


def bfs(r):
    queue = deque([r])
    cnt = 1
    visited[r] = cnt

    while queue:
        cv = queue.popleft()
        for nv in data[cv]:
            if not visited[nv]:
                cnt += 1
                visited[nv] = cnt
                queue.append(nv)


n, m, r = map(int, input().split())
visited = [0] * (n + 1)
data = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    data[u].append(v)
    data[v].append(u)
for i in range(1, n + 1):
    data[i].sort()
bfs(r)

for i in range(1, n + 1):
    print(visited[i])
