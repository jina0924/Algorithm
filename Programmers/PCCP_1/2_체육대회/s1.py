import sys
sys.stdin = open('input2.txt')
from itertools import permutations as P

def solution(ability):
    answer = 0
    n, r = len(ability), len(ability[0])
    
    for p in P(range(n), r):
        tmp = 0
        for i in range(r):
            tmp += ability[p[i]][i]
        answer = max(answer, tmp)
    return answer

data = []
while True:
    row = list(map(int, input().split()))
    if row[0] == 0:
        break
    data.append(row)
print(solution(data))