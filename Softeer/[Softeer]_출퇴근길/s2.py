# 소프티어 HSAT 6회 출퇴근길

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict, deque


def bfs(v, visited):
    queue = deque([v])

    while queue:
        v = queue.popleft()
        if isStart:
            for nv in graph[v]:
                if not visited[nv]:
                    visited[nv] = 1
                    queue.append(nv)
        else:
            for nv in graphR[v]:
                if not visited[nv]:
                    visited[nv] = 1
                    queue.append(nv)


n, m = map(int, input().split())            # 정점의 개수, 간선의 개수
graph = defaultdict(list)                   # 정방향 그래프
graphR = defaultdict(list)                  # 역방향 그래프(각 정점에서 도착지까지 갈 수 있는지 확인용)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graphR[y].append(x)
s, t = map(int, input().split())

isStart = True                              # 정방향 그래프 사용
fromS = [0] * (n + 1)
fromS[t] = 1                                # 도착지에 오면 이동을 멈추므로 미리 방문처리
bfs(s, fromS)

fromT = [0] * (n + 1)
fromT[s] = 1
bfs(t, fromT)

isStart = False
toS = [0] * (n + 1)
bfs(s, toS)

toT = [0] * (n + 1)
bfs(t, toT)

cnt = 0
for i in range(1, n + 1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        if i != s and i != t:
            cnt += 1
print(cnt)