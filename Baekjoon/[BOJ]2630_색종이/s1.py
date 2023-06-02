# 백준 2630번 색종이

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def cut(sr, sc, isBlue, l):
    global white, blue
    isSameColor = True
    for r in range(sr, sr + l):
        for c in range(sc, sc + l):
            if paper[r][c] != isBlue:
                isSameColor = False
                r += l                      # 이중for문 끝내기 위해 r값을 for문이 돌지 않을만큼으로 만듦
                break
    if not isSameColor:
        nl = l // 2
        nr, nc = sr + nl, sc + nl
        cut(sr, sc, paper[sr][sc], nl)
        cut(sr, nc, paper[sr][nc], nl)
        cut(nr, sc, paper[nr][sc], nl)
        cut(nr, nc, paper[nr][nc], nl)
    else:
        if isBlue:
            blue += 1
        else:
            white += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0
cut(0, 0, paper[0][0], N)
print(white)
print(blue)