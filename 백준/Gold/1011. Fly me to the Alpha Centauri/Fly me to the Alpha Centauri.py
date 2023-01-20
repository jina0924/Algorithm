import sys

t = int(input())

for i in range(t):
    x, y = map(int, sys.stdin.readline().split())
    d = y - x
    n = 0
    while d > n*(n+1):
        n += 1
        
    if d <= n**2:
        print(n*2 - 1)
        
    else:
        print(n*2)