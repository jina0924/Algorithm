# 백준 2468번 안전영역

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def bfs(r, c, h):
    queue = deque([(r, c)])
    visited[r][c] = h

    while queue:
        cr, cc = queue.popleft()
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < n and 0 <= nc < n and data[nr][nc] > h and visited[nr][nc] < h:
                visited[nr][nc] = h
                queue.append((nr, nc))

    return 1


n = int(input())
data = []
ans, min_h, max_h = 1, 100, 0

for _ in range(n):
    row = list(map(int, input().split()))
    min_h, max_h = min(*row, min_h), max(*row, max_h)
    data.append(row)

visited = [[0] * n for _ in range(n)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
for h in range(min_h, max_h):
    cnt = 0
    for r in range(n):
        for c in range(n):
            if data[r][c] > h and visited[r][c] < h:
                cnt += bfs(r, c, h)
    ans = max(ans, cnt)

print(ans)