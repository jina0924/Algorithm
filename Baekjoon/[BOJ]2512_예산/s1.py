# 백준 2512번 예산

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n = int(input())                            # 지방의 수
data = list(map(int, input().split()))      # 각 지방의 예산요청
m = int(input())                            # 총 예산
left, right = 0, max(data)
while left <= right:                        # 이분탐색
    mid = (left + right) // 2
    total = 0
    for budget in data:
        if budget <= mid:
            total += budget
        else:
            total += mid
    if total <= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)