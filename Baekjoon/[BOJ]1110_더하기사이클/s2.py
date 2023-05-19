# 백준 1110번 더하기 사이클

N = int(input())
N1 = N
count = 0
while True:
    N2 = (N1 // 10) + (N1 % 10)
    N1 = ((N1 % 10) * 10) + (N2 % 10)
    count += 1

    if N == N1:
        print(count)
        break