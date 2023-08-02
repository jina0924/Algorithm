# 백준 10773번 제로

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

K = int(input())
nums = []
for _ in range(K):
    n = int(input())
    if n == 0:
        nums.pop()
    else:
        nums.append(n)
print(sum(nums))