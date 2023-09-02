# 프로그래머스 PCCP 모의고사 1회 4번 운영체제

import heapq


def solution(program):
    answer = [0] * 11
    program.sort(key=lambda x: (x[1], x[0]))
    waiting = []
    cur = 0
    i = 0

    def call(i):
        while i < len(program) and program[i][1] <= cur:
            heapq.heappush(waiting, program[i])
            i += 1
        return i

    while i < len(program) or waiting:
        if not waiting:
            cur = program[i][1]
            i = call(i)

        j, st, l = heapq.heappop(waiting)
        answer[j] += cur - st
        cur += l
        i = call(i)
    answer[0] += cur

    return answer

import sys
sys.stdin = open('input1.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
print(solution(data))