# 백준 18110번 solved.ac

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
data = sorted([int(input()) for _ in range(n)])
exp = n * 0.15
# 파이썬 내장함수 round()는 오사오입이므로 사사오입을 직접 구현해야함
exp = int(exp) if exp - int(exp) < 0.5 else int(exp) + 1
total = 0
for i in range(exp, n - exp):
    total += data[i]
if n == 0:
    print(0)
else:
    result = (total / (n - 2 * exp))
    if result - int(result) < 0.5:
        print(int(result))
    else:
        print(int(result) + 1)