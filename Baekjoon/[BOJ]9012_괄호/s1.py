# 백준 9012번 괄호

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    data = input().rstrip()
    stack = []
    isVPS = True
    for char in data:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                isVPS = False
                break
    if stack:
        isVPS = False
    print('YES' if isVPS else 'NO')