# 백준 2584번 영역 구하기

import sys
input = sys.stdin.readline


dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def bfs(r, c):
    queue = [(r, c)]
    matrix[r][c] = 1
    cnt = 1

    while queue:
        cr, cc = queue.pop(0)
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < M and 0 <= nc < N and not matrix[nr][nc]:
                matrix[nr][nc] = 1
                queue.append((nr, nc))
                cnt += 1
    ans.append(cnt)


M, N, K = map(int, input().split())
matrix = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(M - y2, M - y1):
        for c in range(x1, x2):
            matrix[r][c] = 1
ans = []
for r in range(M):
    for c in range(N):
        if matrix[r][c] == 0:
            bfs(r, c)
print(len(ans))
print(*sorted(ans))