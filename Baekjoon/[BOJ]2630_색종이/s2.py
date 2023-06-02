# 백준 2630번 색종이

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def cut(sr, sc, l):
    global white, blue
    isBlue = paper[sr][sc]
    for r in range(sr, sr + l):
        for c in range(sc, sc + l):
            if paper[r][c] != isBlue:
                nl = l // 2
                nr, nc = sr + nl, sc + nl
                cut(sr, sc, nl)
                cut(sr, nc, nl)
                cut(nr, sc, nl)
                cut(nr, nc, nl)
                return
    if isBlue:
        blue += 1
    else:
        white += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0
cut(0, 0, N)
print(white)
print(blue)