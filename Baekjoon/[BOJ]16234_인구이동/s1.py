# 백준 16234번 인구이동

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(r, c):
    queue = [(r, c)]
    visited[r][c] = cnt
    total = population[r][c]

    for cr, cc in queue:
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] < cnt:
                gap = abs(population[nr][nc] - population[cr][cc])
                if gap >= L and gap <= R:
                    visited[nr][nc] = cnt
                    queue.append((nr, nc))
                    total += population[nr][nc]

    if len(queue) <= 1:
        return 0
    else:
        result = total // len(queue)
        for cr, cc in queue:
            population[cr][cc] = result
        return 1


N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]
cnt = 0
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
while True:
    isOpen = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c] < cnt:
                isOpen += bfs(r, c)
    if isOpen:
        cnt += 1
    else:
        print(cnt)
        break