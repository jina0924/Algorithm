#2108 통계학
from sys import stdin
from collections import Counter

n = int(stdin.readline())
num_list = []

for i in range(n):
    num_list.append(int(stdin.readline()))
num_list.sort()

mode = Counter(num_list).most_common()

print(round(sum(num_list) / n))
print(num_list[n // 2])
if len(mode) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])
print(max(num_list) - min(num_list))