# PCCP 기출문제 2번
from collections import deque


def solution(land):
    n, m = len(land), len(land[0])
    data = [0] * m
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)


    def bfs(r, c):
        queue = deque([(r, c)])
        land[r][c] = 0
        cnt = 0
        cols = set()

        while queue:
            cr, cc = queue.popleft()
            cnt += 1
            cols.add(cc)
            for d in range(4):
                nr, nc = cr + dr[d], cc + dc[d]
                if 0 <= nr < n and 0 <= nc < m and land[nr][nc]:
                    land[nr][nc] = 0
                    queue.append((nr, nc))

        return cnt, cols


    for r in range(n):
        for c in range(m):
            if land[r][c]:
                cnt, cols = bfs(r, c)
                for col in cols:
                    data[col] += cnt

    return max(data)


land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
print(solution(land))