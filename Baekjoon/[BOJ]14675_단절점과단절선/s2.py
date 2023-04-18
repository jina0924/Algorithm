# 백준 14675번 단절점과 단절선

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N = int(input())
tree = [[] for _ in range(N + 1)]
edges = [0] * N
for i in range(1, N):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    edges[i] = (a, b)


def isCutVertex(x):
    visited = [0] * (N + 1)
    queue = deque([])
    if x == 1:
        queue.append(2)
    else:
        queue.append(1)

    while queue:
        cv = queue.popleft()
        for nv in tree[cv]:
            if nv != x and not visited[nv]:
                visited[nv] = 1
                queue.append(nv)
    if sum(visited) < N - 1:
        print('yes')
    else:
        print('no')


def isCutBrridge(k):
    visited = [0] * (N + 1)
    x, y = edges[k][0], edges[k][1]
    queue = deque([x])

    while queue:
        cv = queue.popleft()
        for nv in tree[cv]:
            if nv != y and not visited[nv]:
                visited[nv] = 1
                queue.append(nv)
    if sum(visited) < N - 1:
        print('yes')
    else:
        print('no')


q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        isCutVertex(k)
    else:
        isCutBrridge(k)