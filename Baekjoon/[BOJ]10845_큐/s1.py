# 백준 10845번 큐

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
queue = []
for _ in range(n):
    data = input().split()
    cmd = data[0]
    if cmd == 'push':
        queue.append(data[1])
    elif cmd == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == 'back':
        if queue:
            print(queue[len(queue) - 1])
        else:
            print(-1)