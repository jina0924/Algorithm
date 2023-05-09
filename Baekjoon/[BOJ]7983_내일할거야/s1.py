# 백준 7983번 내일 할거야

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())                        # 과제의 개수
tasks = []                              # (과제 시작일, 과제 제출일) 담을 리스트
for _ in range(n):
    d, t = map(int, input().split())    # 과제 d일 걸림, t일 안에 풀어야함
    tasks.append((t, t - d + 1))        # 마감일 늦은 순으로 정렬하기 위해
tasks.sort(reverse=True)
start = tasks[0][0] + 1                 # 과제 시작해야되는 날짜 담을 변수
for task in tasks:
    if start <= task[0]:                # 과제해야 하는 날이 겹치는 경우
        start = task[1] - (task[0] - start + 1)     # 시작일 앞당기기기
    else:
        start = task[1]
print(start - 1)