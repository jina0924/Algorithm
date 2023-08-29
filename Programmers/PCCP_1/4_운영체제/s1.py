# 프로그래머스 PCCP 모의고사 1회 4번 운영체제

import heapq

def solution(program):
    answer = [0] * 11
    program.sort(key = lambda x: (x[1], x[0]))
    standby = []
    et = program[0][1]
    i = 0


    def out(et):
        j, st, l = heapq.heappop(standby)
        answer[0] += l
        answer[j] += et - st
        et += l
        return et


    while i < len(program):
        if program[i][1] <= et:
            heapq.heappush(standby, program[i])
            i += 1
        else:
            et = out(et)
    while standby:
        et = out(et)
    return answer

import sys
sys.stdin = open('input2.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
print(solution(data))