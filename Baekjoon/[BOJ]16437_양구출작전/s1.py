# 백준 16437번 양 구출 작전 - 43% 메모리초과

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(130000)
from collections import defaultdict


def dfs(v):
    res = 0
    for nv in tree[v]:
        res += dfs(nv)
    if islands[v][0] == 'W':
        res -= islands[v][1]
        if res < 0:
            res = 0
    else:
        res += islands[v][1]
    return res


n = int(input())
tree = defaultdict(list)
islands = [[], [0, 0]]
for i in range(2, n + 1):
    t, a, p = input().split()
    tree[int(p)].append(i)
    islands.append([t, int(a)])

print(dfs(1))