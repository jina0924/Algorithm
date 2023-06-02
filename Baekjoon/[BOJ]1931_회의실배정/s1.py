# 백준 1931번 회의실 배정

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
schedules = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
# schedules.sort(key=lambda x: x[0])
end, cnt = -1, 0
for meeting in schedules:
    s, e = meeting
    if s >= end:
        end = e
        cnt += 1
print(cnt)