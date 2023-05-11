# 백준 1717번 집합의 표현

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)      # 파이썬의 재귀 최대 깊이 기본 설정이 1000회 => 임의로 늘려줌(주의: PyPy에서는 불가)


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    px, py = find(x), find(y)
    p[px] = py


n, m = map(int, input().split())
p = [i for i in range(n + 1)]
for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')