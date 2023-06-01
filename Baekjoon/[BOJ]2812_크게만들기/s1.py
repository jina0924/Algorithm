# 백준 2812번 크게 만들기

import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
num = list(map(int, input()))
left, right = 0, 1
while k:
    while right < n:
        if num[right] < 0:
            right += 1
            continue
        elif num[left] < num[right]:
            num[left] = -1
            k -= 1
            if k <= 0:
                break
        left += 1
        right += 1
    left, right = 0, 1
ans = 0
point = 1
for i in range(n - 1, -1, -1):
    if num[i] >= 0:
        ans += num[i] * point
        point *= 10
print(ans)