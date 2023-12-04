# 21939번 문제 추천 시스템 version1

import sys
sys.stdin = open('input.txt')
import heapq


def solved_max_out():
    while not questions[-Mheap[0][1]]:
        heapq.heappop(Mheap)


def solved_min_out():
    while not questions[mheap[0][1]]:
        heapq.heappop(mheap)


n = int(input())
mheap = []                              # 난이도 쉬운 순으로 담을 힙
Mheap = []                              # 난이도 어려운 순으로 담을 힙
questions = {}                          # 문제 푼 여부 확인용(안 푼 문제=1, 푼 문제=0)
for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(mheap, (l, p))
    heapq.heappush(Mheap, (-l, -p))
    questions[p] = 1
m = int(input())
for _ in range(m):
    data = input().split()
    r = data[0]
    if r == 'recommend':
        if data[1] == '1':
            solved_max_out()
            print(-Mheap[0][1])
        else:
            solved_min_out()
            print(mheap[0][1])
    elif r == 'add':
        p, l = map(int, data[1:])
        solved_max_out()
        solved_min_out()
        heapq.heappush(mheap, (l, p))
        heapq.heappush(Mheap, (-l, -p))
        questions[p] = 1
    else:
        p = int(data[1])
        questions[p] = 0