# 백준 25206번 너의 평점은

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def sub_score(g):
    score = 0
    if g == 'F':
        return 0
    if g[1] == '+':
        score += 0.5
    if g[0] == 'A':
        score += 4
    elif g[0] == 'B':
        score += 3
    elif g[0] == 'C':
        score += 2
    elif g[0] == 'D':
        score += 1
    return score


total = 0
cnt = 0
for _ in range(20):
    sub, credit, grade = input().split()
    if grade == 'P':
        continue
    credit = float(credit)
    cnt += credit
    total += sub_score(grade) * credit

print(total / cnt)