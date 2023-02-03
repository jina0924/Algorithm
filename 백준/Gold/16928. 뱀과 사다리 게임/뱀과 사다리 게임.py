# 백준 16928번 뱀과 사다리 게임


def bfs():
    queue = [1]
    visited[1] = 1

    while queue:
        s = queue.pop(0)
        if s == 100:
            return visited[100] - 1
        for d in range(1, 7):
            if 0 < s + d <= 100 and not visited[s + d] and not visited[game[s + d]]:
                visited[s + d] = visited[game[s + d]] = visited[s] + 1
                queue.append(game[s + d])


N, M = map(int, input().split())
game = [i for i in range(101)]
visited = [1] + [0] * 100
for _ in range(N):
    x, y = map(int, input().split())
    game[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    game[u] = v
ans = bfs()
print(ans)