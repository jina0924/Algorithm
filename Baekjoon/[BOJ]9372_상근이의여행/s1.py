# 백준 9372번 상근이의 여행

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
    print(N-1)