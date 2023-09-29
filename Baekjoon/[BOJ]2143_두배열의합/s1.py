# 백준 2143번 두 배열의 합

import sys
sys.stdin = open('input.txt')
from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
subsum = defaultdict(int)
for i in range(n + 1):
    for j in range(i):
        subsum[sum(A[j:i])] += 1
ans = 0
m = int(input())
B = list(map(int, input().split()))
for i in range(m + 1):
    for j in range(i):
        ans += subsum[T - sum(B[j:i])]
print(ans)