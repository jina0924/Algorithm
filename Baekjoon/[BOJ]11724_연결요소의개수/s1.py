# 백준 11724번 연결 요소의 개수

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution():
    ans = 0


    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]


    def union(x, y):
        px, py = find(x), find(y)
        p[py] = p[px]


    n, m = map(int, input().split())
    p = [i for i in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        union(u, v)
    for i in range(1, n + 1):
        p[i] = find(p[i])
    ans = len(set(p)) - 1
    return ans

print(solution())