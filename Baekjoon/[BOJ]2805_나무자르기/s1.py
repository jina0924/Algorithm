# 백준 2805번 나무 자르기

import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())        # 나무의 수, 필요한 나무 길이
trees = sorted(list(map(int, input().split())), reverse=True)
ans = 0
ssum = 0
for i in range(n):
    ssum += trees[i]
    if ssum - m < 0:                    # 더 많은 나무 필요하므로 다음 나무로 넘어가기
        continue
    h = (ssum - m) // (i + 1)           # (tree1 - h) + (tree2 - h) + ... = m인 h값 구하기
    if h < ans:                         # 최대값 구했으면 for문 끝내기
        break
    ans = h
print(ans)