# 백준 5052번 전화번호 목록

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = sorted(list(input().rstrip() for _ in range(n)))     # 문자열은 sort시 사전순으로 정렬됨 => 인접한 번호들만 비교하면 일관성 여부 확인 가능
    ans = 'YES'
    for i in range(n - 1):
        l, tlno = len(nums[i]), nums[i]
        if tlno == nums[i + 1][:l]:
            ans = 'NO'
            break
    print(ans)