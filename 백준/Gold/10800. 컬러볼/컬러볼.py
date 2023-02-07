# 백준 10800번 컬러볼 - 시간초과

import sys
input = sys.stdin.readline

N = int(input())
balls = [[i] + list(map(int, input().split())) for i in range(N)]
balls.sort(key=lambda x: x[2])
ans = [0] * N
i = 0
total = 0
color = [0] * (N + 1)
for j in range(1, N):
    while balls[i][2] < balls[j][2]:
        total += balls[i][2]
        color[balls[i][1]] += balls[i][2]
        i += 1
    ans[balls[j][0]] += total - color[balls[j][1]]
print(*ans, sep='\n')