# 백준 15654번 N과 M(5)

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def seq(arr, cnt):
    if cnt < m:
        for j in range(n):
            if nums[j] not in arr:
                seq(arr + [nums[j]], cnt + 1)
    else:
        print(*arr)
        return


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
for i in range(n):
    seq([nums[i]], 1)