# 백준 3107번 IPv6

import sys
sys.stdin = open('input.txt')

IPv6 = input().split(':')
length = len(IPv6)
ans = []
for i in range(length):
    if IPv6[i] == '' and i != 0 and i != length - 1:
        for j in range(9 - length):
            ans.append("0000")
    else:
        ans.append(IPv6[i].zfill(4))
print(':'.join(ans))