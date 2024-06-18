# 백준 15654번 N과 M(5)

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import permutations as P


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
for p in P(nums, m):
    print(*p)