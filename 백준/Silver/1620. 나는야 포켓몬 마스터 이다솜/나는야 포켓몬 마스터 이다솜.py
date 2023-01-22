import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokedex_num = {}
pokedex_name = {}
for i in range(1, N+1):
    pokemon = input().rstrip()
    pokedex_num[i] = pokemon
    pokedex_name[pokemon] = i
for _ in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(pokedex_num.get(int(q)))
    else:
        print(pokedex_name.get(q))