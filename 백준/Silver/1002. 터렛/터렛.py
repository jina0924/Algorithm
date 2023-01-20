from sys import stdin
import math

t = int(stdin.readline())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().split())
    d = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    if r1 + r2 < d or abs(r1 - r2) > d and d > 0:
        print(0)
    elif r1 + r2 == d or abs(r1 - r2) == d and d > 0:
        print(1)
    elif r1 + r2 > d and abs(r1 - r2) < d:
        print(2)
    elif d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)