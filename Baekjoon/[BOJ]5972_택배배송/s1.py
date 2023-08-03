# 백준 5972번 택배 배송

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict
import heapq


def dijkstra(v):
    # 1에서 N까지 가는 최소비용 구하기
    heap = [(0, v)]
    dist[1] = 0

    while heap:
        cw, cv = heapq.heappop(heap)
        # N에 도착하면 끝
        if cv == N:
            print(dist[cv])
            return
        # 이전에 살펴본 현재 위치까지 비용이 더 적다면 지금 들고온 비용 버리기
        if dist[cv] < cw:
            continue
        for nv, nw in data[cv]:
            # 인접한 위치까지의 비용이 현재 위치에서 가는 것보다 크다면 갱신해주기
            if dist[nv] > cw + nw:
                nw += cw
                dist[nv] = nw
                heapq.heappush(heap, (nw, nv))


N, M = map(int, input().split())
data = defaultdict(list)
dist = [sys.maxsize] * (N + 1)
for _ in range(M):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
    data[b].append((a, c))
dijkstra(1)