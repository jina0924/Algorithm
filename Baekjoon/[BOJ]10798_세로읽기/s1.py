# 백준 10798번 세로읽기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

data = []
col = 0
for _ in range(5):
    word = list(input().rstrip())
    col = max(col, len(word))
    data.append(word)
ans = ''
c = 0
while c < col:
    for r in range(5):
        if c < len(data[r]):
            ans += data[r][c]
    c += 1
print(ans)