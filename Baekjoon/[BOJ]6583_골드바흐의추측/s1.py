# 백준 6588번 골드바흐의 추측

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


maxN = 10 ** 6
isPrime = [0, 0] + [1 for _ in range(maxN - 1)]
for x in range(2, int(maxN ** 0.5) + 1):                # n = a + b를 만들 때 a <= b이어야 하므로 제곱근maxN까지만 순회
    if isPrime[x]:
        for y in range(2 * x, maxN + 1, x):
            isPrime[y] = 0

while True:
    n = int(input())
    if n == 0:
        sys.exit()
    for a in range(3, n):
        if isPrime[a] and isPrime[n - a]:
            print(f'{n} = {a} + {n - a}')
            break