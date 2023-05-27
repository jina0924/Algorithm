# 백준 11723번 집합

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

m = int(input())
S = set()
for _ in range(m):
    cmd = input().rstrip()
    if ' ' in cmd:
        cmd, num = cmd.split()
        num = int(num)
    if cmd == 'add':
        S.add(num)
    elif cmd == 'remove':
        if num in S:
            S.remove(num)
    elif cmd == 'check':
        print(int(num in S))
    elif cmd == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif cmd == 'all':
        S = set(range(1, 21))
    else:
        S = set()