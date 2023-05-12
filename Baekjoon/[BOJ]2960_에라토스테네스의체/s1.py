# 백준 2960번 에라토스테네스의 체

import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
nums = set(i for i in range(2, n + 1))
cnt = 0
for a in range(2, n + 1):
    for b in range(1, int(n ** 1 / 2) + 1):
        num = a * b
        if num in nums:
            nums.remove(num)
            cnt += 1
            if cnt == k:
                print(num)
                sys.exit()