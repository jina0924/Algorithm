# 백준 2343번 기타 레슨

import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
'''
강의 순서 유지
i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의도 블루레이에 녹화해야함
블루레이 개수 가급적 줄이기
블루레이 크기를 최소로
M개의 블루레이는 모두 같은 크기
가능한 블루레이의 크기 중 최소 구하시오.
'''
data = list(map(int, input().split()))
left, right = max(data), sum(data)
ans = right
while left <= right:
    mid = (left + right) // 2
    tmp, cnt = 0, 0
    for i in range(len(data)):
        if tmp + data[i] > mid:
            cnt += 1
            tmp = 0
        tmp += data[i]
    if cnt > M:
        left = mid + 1
    else:
        right = mid - 1
    ans = min(ans, mid)
print(left)