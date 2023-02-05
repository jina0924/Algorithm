# 백준 1389번 케빈 베이컨의 6단계 법칙

def kevin_bacon(person):
    queue = [person]
    visited = [0] * (n+1)
    visited[person] = 1

    while queue:
        person = queue.pop(0)
        for i in range(n+1):
            if Graph[person][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[person] + 1

    return sum(visited) - n

n, m = map(int, input().split())
Graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    Graph[a][b] = Graph[b][a] = 1
total = kevin_bacon(1)
ans = 1
for i in range(2, n+1):
    if total > kevin_bacon(i):
        total = kevin_bacon(i)
        ans = i
print(ans)