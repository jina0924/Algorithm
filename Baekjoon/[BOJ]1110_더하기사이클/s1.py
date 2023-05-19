# 백준 1110번 더하기 사이클

import sys
sys.stdin = open('input.txt')

N = input()
if len(N) <= 1:
    N = '0' + N
n = N
cnt = 0
while True:
    cnt += 1
    ssum = str(sum(map(int, n)))
    result = n[-1] + ssum[-1]
    if result == N:
        print(cnt)
        break
    n = result
