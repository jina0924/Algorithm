# 21939번 문제 추천 시스템 version1

import sys
sys.stdin = open('input.txt')
import heapq

n = int(input())
heap = []
for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappop((l, p))
m = int(input())
for _ in range(m):
    data = list(input())
    r = data[0]
    if r == 'recommend':
        pass
    elif r == 'add':
        pass
    else:
        pass