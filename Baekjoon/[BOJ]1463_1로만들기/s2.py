# 백준 1463번 1로 만들기 - 시간초과

import sys
sys.stdin = open('input.txt')

X = int(input())
def calc(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 3 == 0:
        if n % 2:
            ans = min(calc(n // 3) + 1, calc(n - 1) + 1)
        else:
            ans = min(calc(n // 3) + 1, calc(n // 2) + 1)
    elif n % 3 == 1:
        if n % 2:
            ans = calc(n - 1) + 1
        else:
            ans = min(calc(n // 2) + 1, calc(n - 1) + 1)
    else:
        if n % 2:
            ans = calc(n - 1) + 1
        else:
            ans = min(calc(n // 2) + 1, calc(n - 1) + 1)
    return ans
print(calc(X))