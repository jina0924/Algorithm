# 백준 2528번 사다리

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from math import ceil

N, L = map(int, input().split())
building = [[0, 0, 0] for _ in range(N)]
ans = 0
for i in range(N):
    l, d = map(int, input().split())
    if d == 0:
        building[i] = [0, l - 1, d]
    else:
        building[i] = [L - l - 2, L - 1, d]
    if i > 0:
        if building[i - 1][1] < building[i][0] or building[i - 1][0] > building[i][1]:
            if building[i - 1][2] == 0:
                move = (building[i][0] - building[i - 1][1]) // 2 + (building[i][0] - building[i - 1][1]) % 2
                # print(building[i-1], building[i], move)
                building[i - 1][0] += move
                building[i - 1][1] += move
                building[i][0] -= move
                building[i][1] -= move
                ans += move
            else:
                move = (building[i - 1][0] - building[i][1]) // 2 + (building[i][0] - building[i - 1][1]) % 2
                # print(move)
                building[i - 1][0] -= move
                building[i - 1][1] -= move
                building[i][0] += move
                building[i][1] += move
                ans += move
# print(ans)