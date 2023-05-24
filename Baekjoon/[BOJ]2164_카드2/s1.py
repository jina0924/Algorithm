# 백준 2164번 카드2

from collections import deque

n = int(input())
queue = deque([i for i in range(n, 0, -1)])
while queue:
    a = queue.pop()
    if queue:
        queue.appendleft(queue.pop())
print(a)