# 백준 16120번 PPAP

import sys
sys.stdin = open('input.txt')

string = list(input())
PPAP = ['P', 'P', 'A', 'P']
result = []
for char in string:
    result.append(char)
    if len(result) >= 4 and result[-4:] == PPAP:
        for _ in range(3):
            result.pop()
if result == ['P']:
    print('PPAP')
else:
    print('NP')