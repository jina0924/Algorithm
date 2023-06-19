# 백준 3085번 사탕 게임 - 2% x

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from copy import deepcopy


def bfs(cr, cc):
    global ans

    isChanged = False
    data = deepcopy(candies)

    # 가로로 보기
    for sd in (0, -1, 1):
        sr = cr + sd
        cnt = 0
        if 0 <= sr < N:
            color = data[sr][cc]
            if sd != 0:
                isChanged = True
                data[cr][cc], data[sr][cc] = data[sr][cc], data[cr][cc]
        for nc in range(cc, N):
            if data[cr][nc] == color:
                cnt += 1
            else:
                if isChanged:
                    break
                else:
                    for dr, dc in (1, 0), (0, 1):
                        nr, nnc = cr + dr, nc + dc
                        if 0 <= nr < N and 0 <= nnc < N and data[nr][nnc] == color:
                            isChanged = True
                            data[nr][nnc], data[cr][nc] = data[cr][nc], data[nr][nnc]
                            cnt += 1
                            break
                    else:
                        break
        if isChanged:
            ans = max(ans, cnt)

    # 세로로 보기
    isChanged = False
    data = deepcopy(candies)

    # 가로로 보기
    for sd in (0, -1, 1):
        sc = cc + sd
        cnt = 0
        if 0 <= sc < N:
            color = data[cr][sc]
            if sd != 0:
                isChanged = True
                data[cr][cc], data[cr][sc] = data[cr][sc], data[cr][cc]
        for nr in range(cr, N):
            if data[nr][cc] == color:
                cnt += 1
            else:
                if isChanged:
                    break
                else:
                    for dr, dc in (0, 1), (1, 0):
                        nnr, nc = nr + dr, cc + dc
                        if 0 <= nnr < N and 0 <= nc < N and data[nnr][nc] == color:
                            isChanged = True
                            data[nnr][nc], data[nr][cc] = data[nr][cc], data[nnr][nc]
                            cnt += 1
                            break
                    else:
                        break
        if isChanged:
            ans = max(ans, cnt)



N = int(input())
candies = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            bfs(r, c)
print(ans)