# 백준 20529번 가장 가까운 세 사람의 심리적 거리

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import combinations

T = int(input())
for _ in range(T):
    N = int(input())
    students = list(input().split())
    if N > 32:
        print(0)
        continue
    ans = 4 * 3
    for comb in combinations(students, 3):
        result = 0
        for i in range(3):
            for j in range(i, 3):
                for k in range(4):
                    if comb[i][k] != comb[j][k]:
                        result += 1
        ans = min(ans, result)
    print(ans)