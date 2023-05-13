# 백준 6137번 문자열 생성

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def getString(l, r):
    if l >= r:
        return l - 1, 'mid'
    front, back = string[l], string[r]
    if ord(front) < ord(back):
        return l + 1, 'left'
    elif ord(front) > ord(back):
        return r - 1, 'right'
    else:
        return getString(l + 1, r - 1)


N = int(input())
string = ''
for _ in range(N):
    string += input().rstrip()
l, r = 0, N - 1
T = ''
while l < r:
    idx, position = getString(l, r)
    if position == 'left':
        while l < idx:
            T += string[l]
            l += 1
    elif position == 'right':
        while r > idx:
            T += string[r]
            r -= 1
    else:
        while l < idx:
            T += string[l]
            l += 1
        while r > idx:
            T += string[r]
            r -= 1
        break
if N % 2:
    T += string[l]
for i in range(len(T)):
    print(T[i], end='')
    if i % 80 == 1 and not i == 1:
        print()