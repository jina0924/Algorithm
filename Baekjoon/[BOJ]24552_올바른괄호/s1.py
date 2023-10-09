# 백준 24552번 올바른 괄호

import sys
sys.stdin = open('input.txt')

s = input()
n = len(s)
op, cp = 0, 0               # 여는 괄호 개수, 닫는 괄호 개수
cnt = 0                     # 괄호 완성 여부 확인할 변수
for char in s:
    if char == '(':
        op += 1
        cnt += 1
    else:
        cp += 1
        cnt -= 1
    # 1. 닫는 괄호가 더 많아진 경우 -> 반드시 ')' 하나 빼고 끝내야함 -> 현재 있는 ')' 개수 출력
    if cnt < 0:
        print(cp)
        sys.exit()
    # 올바른 괄호 완성 -> '(' 더 없애면 안되므로 0으로 초기화
    if cnt == 0:
        op = 0
# 1번 경우를 만난 적 없다면 '('가 더 많은 상황 -> '(' 개수 출력
print(op)