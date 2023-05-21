# 백준 9012번 괄호

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    data = input().rstrip()
    cnt = 0
    isVPS = True
    for char in data:
        if char == '(':
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
            else:
                isVPS = False
                break
    if cnt > 0:
        isVPS = False
    print('YES' if isVPS else 'NO')