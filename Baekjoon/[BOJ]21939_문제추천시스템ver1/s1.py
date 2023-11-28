# 21939번 문제 추천 시스템 version1

import sys
sys.stdin = open('input.txt')
import heapq

n = int(input())
heap = []
heap2 = []
questions = {}
for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(heap, (l, p))
    heapq.heappush(heap2, (-l, -p))
    questions[p] = 1
m = int(input())
for _ in range(m):
    data = input().split()
    r = data[0]
    if r == 'recommend':
        if data[1] == '1':
            while not questions[-heap2[0][1]]:
                heapq.heappop(heap2)
            print(-heap2[0][1])
        else:
            while not questions[heap[0][1]]:
                heapq.heappop(heap)
            print(heap[0][1])
    elif r == 'add':
        p, l = map(int, data[1:])
        heapq.heappush(heap, (l, p))
        heapq.heappush(heap2, (-l, -p))
        questions[p] = 1
    else:
        p = int(data[1])
        questions[p] = 0