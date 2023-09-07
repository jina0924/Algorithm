# 백준 21942번 부품 대여장

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from datetime import datetime, timedelta

N, L, F = input().split()       # 정보의 개수, 대여기간, 벌
D, h, m = L[:2], int(L[4:6]), int(L[7:9])
book = {}
member = []
for _ in range(int(N)):
    date, time, P, M = input().split()
    dt = datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
    if book.get((P, N)):
        print(dt - book.get((P, N)), date, time)
        if dt - book.get((P, N)):
            pass
        del book[(P, N)]
    else:
        book[(P, N)] = dt