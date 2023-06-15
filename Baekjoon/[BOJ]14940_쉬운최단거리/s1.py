# 백준 14940번 쉬운 최단거리

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def bfs(r, c):
    dist[r][c] = 0
    queue = deque([(r, c)])
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    while queue:
        cr, cc = queue.popleft()
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] < 0:
                if matrix[nr][nc]:
                    queue.append((nr, nc))
                    dist[nr][nc] = dist[cr][cc] + 1
                else:
                    dist[nr][nc] = 0
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 0 and dist[r][c] < 0:
                dist[r][c] = 0


n, m = map(int, input().split())
sr, sc = 0, 0
matrix = []
dist = [[-1] * m for _ in range(n)]
for r in range(n):
    row = list(map(int, input().split()))
    for c in range(m):
        if row[c] == 2:
            sr, sc = r, c
    matrix.append(row)
bfs(sr, sc)
for row in dist:
    print(*row)