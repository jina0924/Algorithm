# 백준 1406번 에디터

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


left = deque(list(input().rstrip()))
m = int(input())
right = deque([])
for _ in range(m):
    cmd = input().split()
    if cmd[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.popleft())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(cmd[1])

print(*left + right, sep="")