# 백준 4949번 균형잡힌 세상

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    string = input().rstrip()
    stack = []
    ans = 'yes'
    if len(string) == 1 and string[0] == '.':
        sys.exit()
    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                ans = 'no'
                break
            elif stack[-1] == '(':
                stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                ans = 'no'
                break
            elif stack[-1] == '[':
                stack.pop()
    if stack:
        ans = 'no'
    print(ans)