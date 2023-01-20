#체스판 다시 칠하기
n, m = map(int, input().split())
board = []
count = []

for i in range(n):
    board.append(input())

for row in range(n-7):
    for col in range(m-7):
        a, b = 0, 0
        for i in range(row, row+8):
            for j in range(col, col+8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        a += 1
                    else:
                        b += 1
                else:
                    if board[i][j] != 'B':
                        a += 1
                    else:
                        b += 1
        count.append(min(a, b))

print(min(count))