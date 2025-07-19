import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())  # 바구니 개수, 바구니 순서 변경 횟수
baskets = [num for num in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    i, j = i - 1, j - 1
    baskets = baskets[:i] + list(reversed(baskets[i:j+1])) + baskets[j+1:]
print(*baskets)

