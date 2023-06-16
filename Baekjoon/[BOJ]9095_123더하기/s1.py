# 백준 9095번 1, 2, 3 더하기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def cnt(x):
    global ans

    if x == n:
        ans += 1
        return
    elif x > n:
        return
    for a in range(1, 4):
        cnt(x + a)


T = int(input())
for _ in range(T):
    n = int(input())
    ans = 0
    cnt(1)
    cnt(2)
    cnt(3)
    print(ans)