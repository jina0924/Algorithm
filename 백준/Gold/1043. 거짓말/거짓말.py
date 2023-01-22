import sys
input = sys.stdin.readline


N, M = map(int, input().split())
already = set(input().split()[1:])
parties = []

for _ in range(M):
    parties.append(set(input().split()[1:]))

for _ in range(M):
    for party in parties:
        if party & already:
            already = already | party

ans = 0
for i in range(M):
    if not set(parties[i]) & already:
        ans += 1
print(ans)