# PCCP 기출문제 1번

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solution(bandage, health, attacks):
    answer = health
    t, x, y = bandage
    cnt, j = 0, 0

    for i in range(1, attacks[-1][0] + 1):
        if i == attacks[j][0]:
            answer -= attacks[j][1]
            if answer <= 0:
                return -1
            j += 1
            cnt = 0
        else:
            cnt += 1
            if cnt >= t:
                answer = min(health, answer + x + y)
                cnt = 0
            else:
                answer = min(health, answer + x)

    return answer


bandage = list(map(int, input().split()))
health = int(input())
attacks = []
for _ in range(2):
    a, k = map(int, input().split())
    attacks.append([a, k])

print(solution(bandage, health, attacks))