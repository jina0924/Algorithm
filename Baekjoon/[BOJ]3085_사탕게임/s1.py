# 백준 3085번 사탕 게임

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(cr, cc):
    isChanged = False
    result, cnt = 0, 0

    # 가로로 볼 때
    for sr, sc in ((cr, cc), (cr - 1, cc), (cr + 1, cc)):
        if 0 <= sr < N and 0 <= sc < N:
            color = candies[sr][sc]
        if sr + sc != 0:
            isChanged = True
        for nc in range(cc, N):
            if candies[cr][nc] == color:
                cnt += 1
                visited[cr][nc] = 1
            else:
                if not isChanged:
                    for dr, dc in ((-1, 0), (1, 0)):
                        nnr, nnc = cr + dr, nc + dc
                        if 0 <= nnr < N and 0 <= nnc < N and candies[nnr][nnc] == color:
                            cnt += 1
                            isChanged = True
                            break
                    else:
                        nc += 1
                        if nc < N and candies[cr][nc]:
                            cnt += 1
                        break
                else:
                    break
    result = max(result, cnt)
    isChanged = False
    cnt = 0
    # 세로로 볼 떄
    for sr, sc in ((cr, cc), (cr, cc -1), (cr, cc + 1)):
        if 0 <= sr < N and 0 <= sc < N:
            color = candies[sr][sc]
        if sr + sc != 0:
            isChanged = True
        for nr in range(cr, N):
            if candies[nr][cc] == color:
                cnt += 1
                visited[nr][cc] = 1
            else:
                if not isChanged:
                    for dr, dc in ((0, -1), (0, 1)):
                        nnr, nnc = nr + dr, cc + dc
                        if 0 <= nnr < N and 0 <= nnc < N and candies[nnr][nnc] == color:
                            cnt += 1
                            isChanged = True
                            break
                    else:
                        nr += 1
                        if nr < N and candies[nr][cc]:
                            cnt += 1
                        break
                else:
                    break
        result = max(result, cnt)
    return result


N = int(input())
candies = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            ans = max(bfs(r, c), ans)
print(ans)