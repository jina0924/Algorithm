# 백준 2015번 수들의 합 4

import sys
sys.stdin = open('input.txt')
from collections import defaultdict

N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
cnt = {}
ans = 0
for i in range(N + 1):
    arr[i] += arr[i - 1]
    ans += cnt.get(arr[i] - K, 0)
    cnt[arr[i]] = cnt.get(arr[i], 0) + 1
print(ans)