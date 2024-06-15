# 백준 1012번 유기농 배추

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    field[x][y] = 0

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < m and 0 <= ny < n and field[nx][ny]:
                queue.append((nx, ny))
                field[nx][ny] = 0
    return 1

T = int(input())
for tc in range(T):
    m, n, k = map(int, input().split())
    field = [[0] * n for _ in range(m)]
    cabagges = []
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1
        cabagges.append((x, y))

    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    for x, y in cabagges:
        if field[x][y]:
            cnt += bfs(x, y)
    print(cnt)