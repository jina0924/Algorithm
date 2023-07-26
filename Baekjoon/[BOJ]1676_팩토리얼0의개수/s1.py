# 백준 1676번 팩토리얼 0의 개수

import sys
sys.setrecursionlimit(1000)


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


def cnt_zero(n):
    n = factorial(n)
    cnt = 0
    while True:
        if n % 10 == 0:
            n //= 10
            cnt += 1
        else:
            print(cnt)
            return


N = int(input())
cnt_zero(N)