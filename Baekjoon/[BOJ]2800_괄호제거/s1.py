# 백준 2800번 괄호 제거

import sys
sys.stdin = open('input.txt')
from itertools import combinations as C
from collections import defaultdict

data = input()
brackets = defaultdict(list)

tmp = 1
for idx in range(len(data)):
    if data[idx] == '(':
        brackets[tmp].append(idx)
        tmp += 1
    elif data[idx] == ')':
        tmp -= 1
        brackets[tmp].append(idx)

ans = []
cnt = len(brackets)
for n in range(1, cnt + 1):
    comb = C(brackets.keys(), n)
    for c in comb:
        result = list(data)
        for j in c:
            s, e = brackets[j]
            result[s], result[e] = '', ''
        ans.append(''.join(result))

for a in sorted(ans):
    print(a)