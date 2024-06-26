# 백준 2644번 촌수

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict, deque


def bfs(s, e):
    queue = deque([(s, 0)])
    visited = [0] * (n + 1)
    visited[s] = 1

    while queue:
        v, cnt = queue.popleft()
        for nv in family[v]:
            if nv == e:
                return cnt + 1
            if not visited[nv]:
                visited[nv] = 1
                queue.append((nv, cnt + 1))

    return -1


n = int(input())
a, b = map(int, input().split())
m = int(input())
family = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)
print(bfs(a, b))