# 백준 1003번 피보나치 함수

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def fibo(n):
    if n == 0:
        return memo[0]
    elif n == 1:
        return memo[1]
    if not memo.get(n):
        tmp1 = fibo(n - 1)
        tmp2 = fibo(n - 2)
        memo[n] = [tmp1[0] + tmp2[0], tmp1[1] + tmp2[1]]
    return memo[n]


T = int(input())
memo = {0: [1, 0], 1: [0, 1]}           # [0이 출력되는 횟수, 1이 출력되는 횟수]
for tc in range(T):
    N = int(input())
    print(*fibo(N))