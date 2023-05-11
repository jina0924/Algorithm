# 백준 16120번 PPAP

import sys
sys.stdin = open('input.txt')

string = input()
ans = 'PPAP'
cnt = 0
if len(string) % 3 == 1:
    for i in range(len(string)):
        if string[i] == 'A':
            if i + 1 < len(string) and string[i + 1] == 'P' and cnt >= 2:
                cnt -= 2
            else:
                ans = 'NP'
                break
        else:
            cnt += 1
else:
    ans = 'NP'
if cnt != 1:
    ans = 'NP'
print(ans)