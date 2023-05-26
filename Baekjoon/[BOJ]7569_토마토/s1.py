# 백준 7569번 토마토

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def bfs():
    new_red = deque([])

    while red:
        ch, cr, cc = red.popleft()
        for d in range(6):
            nh, nr, nc = ch + dh[d], cr + dr[d], cc + dc[d]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and tomatos[nh][nr][nc] == 0:
                new_red.append((nh, nr, nc))
                tomatos[nh][nr][nc] = 1
    return new_red


M, N, H = map(int, input().split())
tomatos = []
red = deque([])
for h in range(H):
    floor = []
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(M):
            if row[c] == 1:
                red.append((h, r, c))
        floor.append(row)
    tomatos.append(floor)
dh, dr, dc = (0, 0, 0, 0, -1, 1), (-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0)
cnt = 0
while red:
    red = bfs()
    if red:
        cnt += 1
for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomatos[h][r][c] == 0:
                print(-1)
                sys.exit()
print(cnt)
